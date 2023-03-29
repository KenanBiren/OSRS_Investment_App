import requests
import time
import pandas as pd
import os
import json

headers = {
    'User-Agent': 'OSRS Investment App Project',
    'From': 'osrsinvestmentproject@gmail.com'
}

# loads current (item id : item name) mapping
def save_map():
    with open('data/map.json', 'r') as file:
        map_dict = json.load(file)
        file.close()
    return map_dict

# creates directory for group if it doesn't exist
def create_group(name_list, mapping, group_id):
    group_id_dict = {}
    name_list.sort()
    new_group = True
    if len(name_list) != 0:
        try:
            os.makedirs('data/groups/' + group_id)
        except FileExistsError:
            new_group = False

        for name in name_list:
            item_id = mapping[name.capitalize()]
            group_id_dict[name] = item_id
        return group_id_dict, new_group

# updates data in group's directory
def update_group_data(group_id_dict, group_id):
    price_dict = {}
    vol_dict = {}
    timestamp_list = []
   
    for interval in ('1h', '6h'): # for both 1 hour and 6 hour intervals
        url = 'https://prices.runescape.wiki/api/v1/osrs/timeseries?timestep=' + interval + '&id='
        for id in group_id_dict.keys():
            time.sleep(2)
            timestamp_list = []
            price_list = []
            vol_list = []
            data_url = url + str(group_id_dict[id])
            data_resp = requests.get(data_url, headers=headers) # get data from api
            data_text = data_resp.json()
            last_hp = 0
            last_lp = 0 # placeholders for the last recorded data point
            last_hv = 0 # (to replace null values from api)
            last_lv = 0

            for point in data_text['data']: # replace null values
                highPrice = last_hp if point['avgHighPrice'] is None else point['avgHighPrice']
                lowPrice = last_lp if point['avgLowPrice'] is None else point['avgLowPrice']
                highVol = last_hv if point['highPriceVolume'] is None else point['highPriceVolume']
                lowVol = last_lv if point['lowPriceVolume'] is None else point['lowPriceVolume']
                last_hp = highPrice
                last_lp = lowPrice
                last_hv = highVol
                last_lv = lowVol
                timestamp_list.append(point['timestamp'])
                price_list.append(int((highPrice + lowPrice) / 2))
                vol_list.append(int((highVol + lowVol) / 2))

            price_dict[id] = price_list # add item's data to price and vol dicts
            vol_dict[id] = vol_list

        price_df = pd.DataFrame.from_dict(price_dict) # save group's data dict as csv
        vol_df = pd.DataFrame.from_dict(vol_dict)
        price_df.index = timestamp_list
        vol_df.index = timestamp_list
        p_path = 'data/groups/' + group_id + '/' + interval + '_price.csv'
        v_path = 'data/groups/' + group_id + '/' + interval + '_vol.csv'
        price_df.to_csv(path_or_buf=p_path, mode='w')
        vol_df.to_csv(path_or_buf=v_path, mode='w')





