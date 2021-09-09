import os, glob
import shutil
import pandas as pd

# /Volumes/Extreme SSD/200_image_data/갈비구이
# folder_list = os.listdir('/Volumes/Extreme SSD/200_image_data/')
folder_list = os.listdir('/Volumes/Extreme SSD/200_data/')

image_list = [i for i in folder_list if not i.endswith('json')]
image_list = sorted(image_list)
json_list = [i for i in folder_list if i.endswith('json')]
json_list = sorted(json_list)

print(len(image_list))
print(len(json_list))
print(json_list)
# for i in image_list:
#     if i =='.DS_Store':
#         continue
#     # for j in os.listdir('/Volumes/Extreme SSD/200_data/'+i):
#     print(len(os.listdir('/Volumes/Extreme SSD/200_data/'+i)))
#         # print(j)
#     if (len(os.listdir('/Volumes/Extreme SSD/200_data/'+i)) != 200):
#         print(i)


def make_filelength_200(data_list) :
    for i in data_list:
        print('folder_name:', i)
        if i =='.DS_Store':
            continue
        file_name_list = os.listdir('/Volumes/Extreme SSD/200_image_data/'+i)
        file_name_list = sorted(file_name_list)
        # print(file_name_list[:10])
        if not os.path.exists('/Volumes/Extreme SSD/200_data/'+i) :
                os.makedirs('/Volumes/Extreme SSD/200_data/'+i)

        for j in file_name_list[:200]:
            shutil.copy('/Volumes/Extreme SSD/200_image_data/'+i+'/'+j, '/Volumes/Extreme SSD/200_data/'+i+'/'+j)

# make_filelength_200(json_list)

def check(class_name) :
    try:
        json_file_list = os.listdir('/Volumes/Extreme SSD/200_data/' + class_name + ' json')
        img_file_list = os.listdir('/Volumes/Extreme SSD/200_data/' + class_name)
        filename_del_json = []
        filename_del_jpg = []

        json_file_list = sorted(json_file_list)
        for i in json_file_list:
            if i =='.DS_Store':
                continue
            filename_del_json.append(i[:-5])

        img_file_list = sorted(img_file_list)
        for i in img_file_list:
            if i =='.DS_Store':
                continue
            filename_del_jpg.append(i[:-4])

        l1 = sorted(filename_del_jpg)
        l1 = set(l1)
        l2 = sorted(filename_del_json)
        l2 = set(l2)
        json_image = l2 - l1
        image_json = l1 - l2

        # print(len(json_image))

        if len(json_image) != 0:
            # if ('.DS_Store' in json_image) & (len(json_image) == 1):
                print('json 파일 - image 파일')
                print(json_image)
        elif len(image_json) != 0 :
            # if ('.DS_Store' in image_json) & (len(image_json) == 1):
                print('image 파일 - json 파일')
                print(image_json)

    except FileNotFoundError:
        print('*파일이 없음*: ' + class_name)

class_name = pd.read_csv('/Users/leeyumin/Downloads/labeling-classname-codename.csv', header=None)
class_name = class_name[1]
# for i in class_name :
#     print('class name: ', i)
#     check(i)

# check('마카로니샐러드')