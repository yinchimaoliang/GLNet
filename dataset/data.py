import os
import random
import shutil
from shutil import copy2
import numpy as np

path1 = '/home1/xilu/projects/data_1_4/images/'
path2 = '/home1/xilu/projects/data_1_4/resize1_4_manual_annotated/'
saveTrainPATH = '/home1/xilu/projects/experiment1/data/train/'
saveValidPATH = '/home1/xilu/projects/experiment1/data/valid/'
saveTestPATH = '/home1/xilu/projects/experiment1/data/test/'


if not os.path.exists(saveTrainPATH+'images/'):
    os.makedirs(saveTrainPATH+'images/')
if not os.path.exists(saveValidPATH+'images/'):
    os.makedirs(saveValidPATH+'images/')
if not os.path.exists(saveTestPATH+'images/'):
    os.makedirs(saveTestPATH+'images/')
if not os.path.exists(saveTrainPATH+'annotations/'):
    os.makedirs(saveTrainPATH+'annotations/')
if not os.path.exists(saveValidPATH+'annotations/'):
    os.makedirs(saveValidPATH+'annotations/')
if not os.path.exists(saveTestPATH+'annotations/'):
    os.makedirs(saveTestPATH+'annotations/')    
dirs = os.listdir(path1)
num = len( dirs)
index_list = np.arange(num)
random.shuffle(index_list)

filename = []
for file in dirs:
    filename.append(file[0:-4])

for i in range(int(num*0.8)):
    shutil.copy(path1+filename[index_list[i]]+'.JPG', saveTrainPATH+'images/'+filename[index_list[i]]+'.png')
    shutil.copy(path2+filename[index_list[i]]+'_mask.png', saveTrainPATH+'annotations/'+filename[index_list[i]]+'.png')

for i in range((int(num*0.8)+1),num):
    shutil.copy(path1+filename[index_list[i]]+'.JPG', saveValidPATH+'images/'+filename[index_list[i]]+'.png')
    shutil.copy(path2+filename[index_list[i]]+'_mask.png', saveValidPATH+'annotations/'+filename[index_list[i]]+'.png')

for i in range((int(num*0.8)+1),num):
    shutil.copy(path1+filename[index_list[i]]+'.JPG', saveTestPATH+'images/'+filename[index_list[i]]+'.png')
    shutil.copy(path2+filename[index_list[i]]+'_mask.png', saveTestPATH+'annotations/'+filename[index_list[i]]+'.png')

'''
#class 4 
shutil.copy(path1+'1021496-6-LYY.JPG', saveValidPATH+'images/1021496-6-LYY.png')
shutil.copy(path2+'1021496-6-LYY_mask.png', saveValidPATH+'annotations/1021496-6-LYY.png')
#class 5
shutil.copy(path1+'1016172-4-LYY.JPG', saveValidPATH+'images/1016172-4-LYY.png')
shutil.copy(path2+'1016172-4-LYY_mask.png', saveValidPATH+'annotations/1016172-4-LYY.png')

shutil.copy(path1+'1016172-3-LYY.JPG', saveTestPATH+'images/1016172-3-LYY.png')
shutil.copy(path2+'1016172-3-LYY_mask.png', saveTestPATH+'annotations/1016172-3-LYY.png')
'''
