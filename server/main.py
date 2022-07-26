import pandas as pd
import os
import glob
import re
import shutil


def reloc(from_path, to_path):
    get_files = os.listdir(from_path)
    for file in get_files:
        shutil.copy2(from_path + '/' + file, to_path)
        os.remove(from_path + '/' + file)



def create_df(files_csv, files_png):
    df = pd.DataFrame(columns=['user_id', 'first_name', 'last_name', 'birthts', 'img_path'])
    for path_csv in files_csv:
        sm_df = pd.read_csv(path_csv)
        user_id = re.search(r'\d*[.]csv', path_csv)
        user_id = user_id[0][:-4]
        img_path = None
        user_png = user_id + '.png'
        for path_png in files_png:
            if user_png in path_png:
                if '\\new_data\\' in path_png:
                    img_path = os.path.abspath('02-src-data') + '\\' + user_png
                else:
                    img_path = path_png
                break
        df.loc[len(df)] = [user_id, sm_df.iat[0, 0], sm_df.iat[0, 1], sm_df.iat[0, 2], img_path]
    return df



if __name__ == '__main__':
    path = os.path.abspath('02-src-data')
    files_csv = glob.glob(path + '/*.csv')
    files_png = glob.glob(path + '/*.png')
    df = create_df(files_csv, files_png)
    df.to_csv('all_data.csv', index=False)



