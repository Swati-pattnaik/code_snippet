# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import fnmatch
import os
import hashlib
from scipy.misc import imread, imresize, imshow
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
%matplotlib inline
import time
import numpy as np

os.chdir('C:\\pics')

def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

os.getcwd()
folder = next(os.walk('.'))[1]
for x in folder:
    file_list = fnmatch.filter(os.listdir(x),'*.jpg')
    len(file_list)
    duplicates = []
    hash_keys = dict()
    for i,filename in enumerate(file_list):
        filehash = file_hash(os.path.join(x,filename))
        if filehash not in hash_keys:
            print(i)
            hash_keys[filehash] = i
        else:

            duplicates = duplicates + [(i,hash_keys[filehash])]

    
#    for file_index in duplicates:
#        try:
#            plt.subplots(121), plt.imshow(imread(file_list[fle_index[1]]))
#            plt.title(file_index[1]), plt.xticks([]), plt.yticks([])
#            plt.subplot(122), plt.imshow(imread(file_list[fle_index[0]]))
#            plt.title(file_index[0]+' duplicates'), plt.xticks([]), plt.yticks([])
#            plt.show()
#        except OSError as e:
#            continue
    
    for i in duplicates:
        os.remove(f'.\\{x}\\{file_list[i[0]]}')
