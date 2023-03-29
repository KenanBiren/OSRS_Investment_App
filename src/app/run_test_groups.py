import group_functions, graph_functions, log_functions
import time
import os


map_dict = group_functions.save_map()

# utility function to keep test group input strings the same as a user would input
def str_resp_to_list(str_resp):
    name_list = []
    if str_resp[0] == '[':
        try:
            name_list_str = str_resp.strip('[,], ')
            add_name_list = name_list_str.split(',')
            for n in range(len(add_name_list)):
                add_name_list[n] = add_name_list[n].strip()
            name_list = name_list + add_name_list
        except:
            print('String response to list conversion failed.')
    return name_list

# make all graphs for all six test groups
def run_all_test_groups():
    timestamp = int(time.time())
    log_functions.start_run_all_test_groups(timestamp)

    testgroup1()
    testgroup2()
    testgroup3()
    testgroup4()
    testgroup5()
    testgroup6()

    timestamp = int(time.time())
    log_functions.end_run_all_test_groups(timestamp)
    return


# common alchables
def testgroup1():
    tg1_common_alchs = "[rune full helm, rune kiteshield, rune platebody, rune platelegs, red d'hide body, green d'hide body, blue d'hide body, black d'hide body, air battlestaff, water battlestaff, earth battlestaff, fire battlestaff, rune javelin heads, dragon javelin heads, onyx bolts (e), dragonstone bolts (e), sapphire necklace, ruby necklace, gold necklace, gold bracelet, magic longbow, yew longbow, maple longbow (u), magic shortbow]"

    id_resp = 'tg1_common_alchs'
    name_list = str_resp_to_list(tg1_common_alchs)


    group = group_functions.create_group(name_list, map_dict, id_resp)
    group_dict = group[0]
    new_group = group[1]
    timestamp = int(time.time())
    if new_group:
        log_functions.create_group_log(timestamp, id_resp)
    group_functions.update_group_data(group_dict, 'both', id_resp)
    timestamp = int(time.time())
    log_functions.update_group_data_log(timestamp, id_resp)

    create_all_graphs(id_resp)
    verify_all_graphs_logs(id_resp)
    return


# rune alchables
def testgroup2():
    tg2_rune_alchs = "[rune chainbody, rune full helm, rune halberd, rune platelegs, rune platebody, rune longsword, rune kiteshield, rune warhammer, rune sq shield, rune hasta, rune spear, rune axe, rune med helm, rune sword, rune 2h sword, rune dagger, rune mace, rune battleaxe, rune scimitar, rune sq shield, runite limbs]"

    id_resp = 'tg2_rune_alchs'
    name_list = str_resp_to_list(tg2_rune_alchs)

    group = group_functions.create_group(name_list, map_dict, id_resp)
    group_dict = group[0]
    new_group = group[1]
    timestamp = int(time.time())
    if new_group:
        log_functions.create_group_log(timestamp, id_resp)
    group_functions.update_group_data(group_dict, 'both', id_resp)
    timestamp = int(time.time())
    log_functions.update_group_data_log(timestamp, id_resp)

    create_all_graphs(id_resp)
    verify_all_graphs_logs(id_resp)
    return


# runes
def testgroup3():
    tg3_runes = "[cosmic rune, chaos rune, astral rune, nature rune, law rune, death rune, blood rune, soul rune, wrath rune]"

    id_resp = 'tg3_runes'
    name_list = str_resp_to_list(tg3_runes)

    group = group_functions.create_group(name_list, map_dict, id_resp)
    group_dict = group[0]
    new_group = group[1]
    timestamp = int(time.time())
    if new_group:
        log_functions.create_group_log(timestamp, id_resp)
    group_functions.update_group_data(group_dict, 'both', id_resp)
    timestamp = int(time.time())
    log_functions.update_group_data_log(timestamp, id_resp)

    create_all_graphs(id_resp)
    verify_all_graphs_logs(id_resp)
    return


# bones
def testgroup4():
    tg4_bones = "[babydragon bones, wyrm bones, dragon bones, lava dragon bones, hydra bones, dagannoth bones, superior dragon bones, drake bones]"

    id_resp = 'tg4_bones'
    name_list = str_resp_to_list(tg4_bones)

    group = group_functions.create_group(name_list, map_dict, id_resp)
    group_dict = group[0]
    new_group = group[1]
    timestamp = int(time.time())
    if new_group:
        log_functions.create_group_log(timestamp, id_resp)
    group_functions.update_group_data(group_dict, 'both', id_resp)
    timestamp = int(time.time())
    log_functions.update_group_data_log(timestamp, id_resp)

    create_all_graphs(id_resp)
    verify_all_graphs_logs(id_resp)
    return


# raw fish
def testgroup5():
    tg5_raw_fish = "[raw karambwan, raw shark, raw sea turtle, raw manta ray, raw dark crab, raw anglerfish]"

    id_resp = 'tg5_raw_fish'
    name_list = str_resp_to_list(tg5_raw_fish)

    group = group_functions.create_group(name_list, map_dict, id_resp)
    group_dict = group[0]
    new_group = group[1]
    timestamp = int(time.time())
    if new_group:
        log_functions.create_group_log(timestamp, id_resp)
    group_functions.update_group_data(group_dict, 'both', id_resp)
    timestamp = int(time.time())
    log_functions.update_group_data_log(timestamp, id_resp)

    create_all_graphs(id_resp)
    verify_all_graphs_logs(id_resp)
    return


# cooked fish
def testgroup6():
    tg6_cooked_fish = "[cooked karambwan, shark, sea turtle, manta ray, dark crab, anglerfish]"

    id_resp = 'tg6_cooked_fish'
    name_list = str_resp_to_list(tg6_cooked_fish)

    group = group_functions.create_group(name_list, map_dict, id_resp)
    group_dict = group[0]
    new_group = group[1]
    timestamp = int(time.time())
    if new_group:
        log_functions.create_group_log(timestamp, id_resp)
    group_functions.update_group_data(group_dict, 'both', id_resp)
    timestamp = int(time.time())
    log_functions.update_group_data_log(timestamp, id_resp)

    create_all_graphs(id_resp)
    verify_all_graphs_logs(id_resp)
    return

# make all graphs for test group with 3% outliers marked
def create_all_graphs(group_id):
    graph_functions.make_plot(group_id, 'p', '1h', 'max', '3', 'raw')
    timestamp = int(time.time())
    log_functions.create_raw_plot_log(timestamp, group_id, 'p', '1h', 'max', '3')
    graph_functions.make_plot(group_id, 'v', '1h', 'max', '3', 'raw')
    timestamp = int(time.time())
    log_functions.create_raw_plot_log(timestamp, group_id, 'v', '1h', 'max', '3')
    graph_functions.make_plot(group_id, 'p', '6h', 'max', '3', 'raw')
    timestamp = int(time.time())
    log_functions.create_raw_plot_log(timestamp, group_id, 'p', '6h', 'max', '3')
    graph_functions.make_plot(group_id, 'v', '6h', 'max', '3', 'raw')
    timestamp = int(time.time())
    log_functions.create_raw_plot_log(timestamp, group_id, 'v', '6h', 'max', '3')

    graph_functions.make_plot(group_id, 'p', '1h', 'max', '3', 'relative')
    timestamp = int(time.time())
    log_functions.create_rel_plot_log(timestamp, group_id, 'p', '1h', 'max', '3')
    graph_functions.make_plot(group_id, 'v', '1h', 'max', '3', 'relative')
    timestamp = int(time.time())
    log_functions.create_rel_plot_log(timestamp, group_id, 'v', '1h', 'max', '3')
    graph_functions.make_plot(group_id, 'p', '6h', 'max', '3', 'relative')
    timestamp = int(time.time())
    log_functions.create_rel_plot_log(timestamp, group_id, 'p', '6h', 'max', '3')
    graph_functions.make_plot(group_id, 'v', '6h', 'max', '3', 'relative')
    timestamp = int(time.time())
    log_functions.create_rel_plot_log(timestamp, group_id, 'v', '6h', 'max', '3')


# verify logs right after a test group's complete run
def verify_all_graphs_logs(group_id):
    raw_msg = 'raw plot created'
    rel_msg = 'relative plot created'
    updt_msg = 'group data updated'
    timeframe = 'max'

    check_dict = {-1:"['v', '6h', 'max', '3']", -2:"['p', '6h', 'max', '3']", -3:"['v', '1h', 'max', '3']", -4:"['p', '1h', 'max', '3']", -5:"['v', '6h', 'max', '3']", -6:"['p', '6h', 'max', '3']", -7:"['v', '1h', 'max', '3']", -8:"['p', '1h', 'max', '3']"}


    with open('data/logs.csv', 'r') as f:
        log = f.readlines()
        for n in check_dict.keys():
            if n >= -4:
                msg = rel_msg
            else:
                msg = raw_msg

            line = log[n]
            if line.split(',')[1] != msg or line.split(',')[2] != group_id or check_dict[n] not in line:
                print('Error. Graphs not properly created for ' + group_id)
    
        f.close()