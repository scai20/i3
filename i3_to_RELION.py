#!/bin/bash
#created by Shujun

import math
import numpy as np
from scipy.spatial.transform import Rotation as R
from scipy.spatial import cKDTree
#import matplotlib as mpl
#from mpl_toolkits.mplot3d import Axes3D
#import numpy as np
#import matplotlib.pyplot as plt

flag = 1

list1 = np.genfromtxt('trf_extract.txt')
#list3 = np.genfromtxt('run_it025_data.txt')
#myfile = open("run_it025_data.txt",'r')
#content = myfile.read()
#content_list = content.split('	')
#print(content_list)
#print(len(content_list))
#print(list3)

array1 =np.asarray(list1)
#print(array1)

list2 = []
for k in range(array1.shape[0]):
	#print(k)
	r1=R.from_euler('zxz', list(array1[k,:3]), degrees=False)
	r2=np.array(r1.as_euler('zyz', degrees=False))
	list2.append(list(r2))
list2 = np.asarray(list2)
#print(list2)
np.savetxt('relion_test.txt',list2)


