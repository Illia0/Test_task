import time
import pandas as pd
import os
import glob
from main import create_df
from main import reloc

while True:
    path = os.path.abspath('new_data')
    files_csv = glob.glob(path + '/*.csv')
    files_png = glob.glob(path + '/*.png')
    new_df = create_df(files_csv, files_png)
    df = pd.read_csv('all_data.csv')
    del_labels = []
    for i in range(len(df)):
        for j in range(len(new_df)):
            if str(df.iat[i, 0]) == new_df.iat[j, 0]:
                del_labels.append(i)
                break
    df.drop(labels=del_labels, axis=0, inplace=True)
    res_df = pd.concat([df, new_df], ignore_index=True)
    res_df.to_csv('all_data.csv', index=False)
    reloc(path, os.path.abspath('02-src-data'))
    time.sleep(600)
