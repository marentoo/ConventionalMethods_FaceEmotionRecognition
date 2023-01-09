import cv2
import numpy as np

import os
from os import listdir
from os.path import isfile, join
from lbp import getLBP

list_folder = []
rootdir = 'dataset/train'

#Filling list_folder of folders to iterate e.g. 'dataset/train\\happy'
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        list_folder.append(d)
#Changing separator from '\' to '/'
list_folder = [list_d.replace(os.sep, '/') for list_d in list_folder]
k=1
#Loading each file through list of folders and using method getLBP on each file
for folder in list_folder:
    onlyfiles = [f for f in listdir(f'{folder}') if isfile(join(f'{folder}', f))][0:2] #tylko 2files z kazdego folderu na probe
    # print('\n'); print(f'{folder}\n', onlyfiles[:2])
    for file in onlyfiles:
        # image_read = cv2.imread(f'{folder}/{file}',cv2.IMREAD_GRAYSCALE)
        image_read = cv2.imread(f'{folder}/{file}',cv2.IMREAD_COLOR)
        # print('\n'); print(f'X: {image_read}')
        im = getLBP(image_read)
        cv2.imshow("Input", im)
        cv2.waitKey(0)
        cv2.imwrite(f'/Users/mat/Desktop/docelowy/Obrazek{k}.jpg',im); k += 1
