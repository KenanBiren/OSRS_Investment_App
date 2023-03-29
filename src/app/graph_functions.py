import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import itertools
import matplotlib.patches as mpatches
import matplotlib.axes as maxes
import matplotlib.ticker as ticker
import os




def plot_preprocess(df, tf_in_days):
    # limits data set by timeframe (in days)
    start_val = int(df['timestamp'].iloc[0]) / 86400
    new_col = df.loc[:, ['timestamp']].div(86400).round(4).subtract(start_val)
    np_col = new_col['timestamp'].to_numpy()
    np.flip(np_col)
    df['timestamp'] = np_col
    df_ltd = df[df['timestamp'] < int(tf_in_days)]

    return df_ltd


def plot(group_id, mode, df, timeframe, outl_perc, filename):
    # plots data set and marks outliers in red
    colors = itertools.cycle(["green", "dimgray", "blue", "darkorange", "mediumorchid", "cyan", "lime", "magenta", "coral", "olive", "yellow", "cornflowerblue", "rosybrown", "lightpink", "silver", "midnightblue"])  # colors for plot points
    col_names = []
    legend_patches = []
    outl_perc = int(outl_perc)
    lower_q = outl_perc * .01
    upper_q = 1 - (outl_perc * .01)

    if timeframe == 'max':  # timeframe limit
        timeframe = 100
        df = plot_preprocess(df, timeframe)  
    else:
        try:
            df = plot_preprocess(df, timeframe)
        except:
            print('Valid timeframe not given.')

    for col in df.columns:
        col_names.append(col)
    col_names.remove('timestamp')

    for col in col_names:  # make plot point by point, marking outliers with red color
        min_threshold = df[col].quantile(lower_q)  # min and max thresholds
        max_threshold = df[col].quantile(upper_q)
        xs = df['timestamp']
        ys = df[col]
        color = next(colors)
        patch = mpatches.Patch(color=color, label=col)
        legend_patches.append(patch)

        for x, y in zip(xs, ys):
            plt.scatter(x, y, s=2, color=color)

            if not min_threshold <= y <= max_threshold:  # condition for being an outlier
                plt.scatter(x, y, s=2, color='red')

    plt.xlabel('days ago')
    if mode == 'p':
        plt.ylabel('price')
    else:
        plt.ylabel('volume')
    plt.title(group_id)
    plt.gca().invert_xaxis()
    plt.legend(handles=legend_patches)
    graph_path = 'data/groups/' + group_id + '/' + filename
    if os.path.isfile(graph_path): # save/replace file if exists
        os.remove(graph_path)
    plt.savefig(graph_path)
    plt.close()



def plot_rel(group_id, mode, df, timeframe, outliers, filename):
    # scales each column of data by it's recent 7-point average
    col_names = []
    for col in df.columns:
        col_names.append(col)
    col_names.remove('timestamp')

    for col in col_names:
        s = df[col]
        outliers = int(outliers)
        lower_q = outliers * .01
        upper_q = 1 - (outliers * .01)
        lb = s.quantile(lower_q)
        ub = s.quantile(upper_q)
        df[col].mask((df[col] < lb) | (df[col] > ub), other=1, inplace=True)

    for col in col_names:
        rct_pts = df[col].tail(8)
        avg = rct_pts.mean()
        df[col] = df[col] / avg



    plot(group_id, mode, df, timeframe, outliers, filename)


def make_plot(group_id, mode, interval, timeframe, outliers, plot_type):
    if mode == 'p':  # use price data
        path = 'data/groups/' + group_id + '/' + interval + '_price.csv'
    elif mode == 'v':  # use volume data
        path = 'data/groups/' + group_id + '/' + interval + '_vol.csv'
    else:
        path = ''
        print('Valid mode not given. Input [p] to use price data or [v] to use volume data')

    # catch if group doesn't exist
    if os.path.isfile('data/groups/' + group_id) is False:
        print('Group with id' + group_id + 'does not exist')
        return
    df = pd.read_csv(path)
    df.rename(columns={df.columns[0]: 'timestamp'}, inplace=True)
    current_ts = int(time.time())

    filename = mode + '_' + interval + '_' + timeframe + '_' + outliers + '_' + plot_type

    # call method to create plot with given parameters
    if plot_type == 'raw':
        plot(group_id, mode, df, timeframe, outliers, filename)
    elif plot_type == 'relative':
        plot_rel(group_id, mode, df, timeframe, outliers, filename)
