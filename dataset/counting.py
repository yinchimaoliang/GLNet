from PIL import Image
import os
import numpy as np
import cv2
flag0=0
flag1=0
flag2=0
flag3=0
flag4=0
f = open("count.txt", "w") 
path = '/home1/xilu/projects/data_1_4/resize1_4_processed_annotated/'
for filename in os.listdir(path):
	#img = Image.open(path+filename)
	img=cv2.imread(path+filename,0)
	i = np.array(img)
	#print(i.shape)
	
	for x in range(i.shape[0]):
		for y in range(i.shape[1]):
			px = i[x,y]
			#print(px)
			if(px==0):
				flag0+=1
			elif(px==1):
				flag1+=1
			elif(px==2):
				flag2+=1
			elif(px==3):
				flag3+=1
			elif(px==4):
				flag4+=1
	print(filename,file=f)
	print(flag0,file=f)
	print(flag1,file=f)
	print(flag2,file=f)
	print(flag3,file=f)
	print(flag4,file=f)

f.close
	






