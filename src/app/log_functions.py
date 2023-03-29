import csv




def create_group_log(timestamp, group_id):
    with open('data/logs.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, 'group created', group_id])
        f.close()
    return

def update_group_data_log(timestamp, group_id):
    with open('data/logs.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, 'group data updated', group_id])
        f.close()
    return

def create_raw_plot_log(timestamp, group_id, mode_resp, ti_resp, tf_resp, outl_resp):
    with open('data/logs.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, 'raw plot created', group_id, [mode_resp, ti_resp, tf_resp, outl_resp]])
        f.close()
    return


def create_rel_plot_log(timestamp, group_id, mode_resp, ti_resp, tf_resp, outl_resp):
    with open('data/logs.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, 'relative plot created', group_id, [mode_resp, ti_resp, tf_resp, outl_resp]])
        f.close()
    return

def start_run_all_test_groups(timestamp):
    with open('data/logs.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, 'test run (all test groups) started'])
        f.close()
    return

def end_run_all_test_groups(timestamp):
    with open('data/logs.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, 'test run (all test groups) ended'])
        f.close()
    return