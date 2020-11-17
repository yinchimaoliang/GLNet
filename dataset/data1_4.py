'''
#select annotated images
import random
import shutil
from shutil import copy2
import numpy as np
import os
path1 = '/home1/xilu/projects/data_1_4/resize_1_4/'
path2 = '/home1/xilu/projects/data_1_4/resize1_4_processed_annotated/'
savepath = '/home1/xilu/projects/data_1_4/images/'
dirs = os.listdir(path2)
for file in dirs:
    shutil.copy(path1+file[0:-9]+'.JPG', savepath + file[0:-9]+'.JPG')
'''

