import group_functions, graph_functions, log_functions, run_test_groups
import time



# command line style prompt for user
def prompt():

    map_dict = group_functions.save_map()
    name_list = []
    running = True
    name_master_list = [i.lower() for i in map_dict.keys()]

    while(running):
        resp = input('Please select an action. Options: Make New Graph [g], Add Item to Group [a], Remove Item from Group [r], Save/Update Group Data [s], Start New Group [n], Run All Test Groups [test], Quit [q]')

        if resp == 'g': # create graph (parameters: raw vs relative, price vs volume, timeframe, % outliers to mark)
            sel_resp = input('Input group id:')
            mode_resp = input('Analyze Price [p] or Volume [v]: ')
            ti_resp = input('Input time interval [1h] or [6h]:')
            tf_resp = input('Input timeframe (number of days or [max]):')
            outl_resp = input('Percentage of outliers to mark:')
            anls_op = input('Select Analysis Type. Options: raw, relative') # 'raw' or 'relative'
            graph_functions.make_plot(sel_resp, mode_resp, ti_resp, tf_resp, outl_resp, anls_op)
            if anls_op == 'raw':
                timestamp = int(time.time())
                log_functions.create_raw_plot_log(timestamp, sel_resp, mode_resp, ti_resp, tf_resp, outl_resp)
            elif anls_op == 'relative':
                timestamp = int(time.time())
                log_functions.create_rel_plot_log(timestamp, sel_resp, mode_resp, ti_resp, tf_resp, outl_resp)

        if resp == 'a': # add item or list of items to group
            add_resp = input('Type in item name or list in [item1,item2...] format to add to group:')
            if add_resp[0] == '[':
                try:
                    name_list_str = add_resp.strip('[,], ')
                    add_name_list = name_list_str.split(',')
                    for n in range(len(add_name_list)):
                        add_name_list[n] = add_name_list[n].strip()
                    name_list = name_list + add_name_list
                except:
                    print('Input error, please check input spelling')
                print('Group: ')
                print(name_list)
            elif add_resp.lower() in name_master_list:
                name_list.append(add_resp)
                print('Item added to group.')
                print('Group: ')
                print(name_list)

                if add_resp in name_list:
                    print('Item already in group.')
                    print('Group: ')
                    print(name_list)
            else:
                print('Valid item name or list not given, please check spelling.')
                print('Group: ')
                print(name_list)

        elif resp == 'r': # remove item from group

            rem_resp = input('Type in item name to remove from group:')

            if rem_resp in name_list:
                name_list.remove(rem_resp)
                print('Successful removal.')
                print('Group: ')
                print(name_list)
            else:
                print('Item is not in group, please check spelling.')
                print('Group: ')
                print(name_list)

        elif resp == 's': # create folder for group and save data for group items

            id_resp = input('Group id:')
            group = group_functions.create_group(name_list, map_dict, id_resp)
            group_dict = group[0]
            new_group = group[1]
            timestamp = int(time.time())
            if new_group:
                log_functions.create_group_log(timestamp, id_resp)
            group_functions.update_group_data(group_dict, id_resp)
            timestamp = int(time.time())
            log_functions.update_group_data_log(timestamp, id_resp)
            print('Data saved for group: ')
            print(name_list)

        elif resp == 'n': # start new group

            name_list = []
            print('Group: ')
            print(name_list)

        elif resp == 'q': # quit session

            print('Ended.')
            running = False
        elif resp == 'test': # run all test groups (all graphs w/ max timeframe and 3% outliers)
            run_test_groups.run_all_test_groups()
        else: # valid input not entered

            print('Please enter a valid option.')
            print('Group: ')
            print(name_list)



prompt()