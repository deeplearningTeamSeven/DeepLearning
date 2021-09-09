import os, glob
import shutil
import pandas as pd
import numpy as np

base_path = '/Volumes/Extreme SSD/건강관리를 위한 음식 이미지/Validation/'
image_list = []
json_list = []
folder_list = os.listdir(base_path)
image_list = [i for i in folder_list if i.endswith('_Val')]
json_list = [i for i in folder_list if i.endswith('_json')]

# print(image_list)

def make_folder(new_path, new_folder):
    global new_dir
    new_dir = new_path + '/' + new_folder + '/'
    try:
        if not os.path.exists(new_dir) :
            os.makedirs(new_dir)
    except OSError:
        print('Error')

def data_move(data_list):
    for i in data_list:
        for j in os.listdir(base_path + i):
            print(base_path+i+'/'+j, '===>', new_dir)
            # print(new_dir)
            try :
                shutil.move(base_path+i+'/'+j, new_dir)
            except shutil.Error:
                print("파일이 이미 존재함: " + j)

# make_folder('/Volumes/Extreme SSD', 'all_image_data')
# make_folder('/Volumes/Extreme SSD/', 'all_json_data')
# data_move(image_list)
# data_move(json_list)


def extract_data_folder(oring_path) :
    class_name = pd.read_csv('/Users/leeyumin/Downloads/labeling-classname-codename.csv', header=None)
    class_name = class_name[1]
    make_folder('/Volumes/Extreme SSD/', 'image_data')
    for i in class_name:
        # print(oring_path+i+' json')
        try :
            shutil.move(oring_path+i, new_dir)
        except shutil.Error:
            print("파일이 이미 존재함: " + i)
        except FileNotFoundError:
            print("파일이 없음"+i)
   
# extract_data_folder('/Volumes/Extreme SSD/all_image_data/')