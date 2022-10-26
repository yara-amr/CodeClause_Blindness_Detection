import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory
import shutil
import sys
import os


train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
print(train_df.shape)
print(test_df.shape)
train_df.head()


list_0=[]
for a in train_df[train_df['diagnosis']==0]['id_code']:
    list_0.append(a)
list_1=[]
for b in train_df[train_df['diagnosis']==1]['id_code']:
    list_1.append(b)
list_2=[]
for c in train_df[train_df['diagnosis']==2]['id_code']:
    list_2.append(c)
list_3=[]
for d in train_df[train_df['diagnosis']==3]['id_code']:
    list_3.append(d)
list_4=[]
for e in train_df[train_df['diagnosis']==4]['id_code']:
    list_4.append(e)
    

train_dir = "train_image/"
    # Create subdirectory with `class_name`
if not os.path.exists("train_split" + "4"):
        os.mkdir("train_split" + "4")
for i in list_4:
    src_path = train_dir + i + ".png"
    dst_path = "train_split" + "4" + "/" + i + ".png"
    shutil.copy(src_path, dst_path)
    
    
 train_dir = "train_image/"
    # Create subdirectory with `class_name`
if not os.path.exists("train_split" + "3"):
        os.mkdir("train_split" + "3")
for i in list_3:
    src_path = train_dir + i + ".png"
    dst_path = "train_split" + "3" + "/" + i + ".png"
    shutil.copy(src_path, dst_path)
    
    
 train_dir = "train_image/"
    # Create subdirectory with `class_name`
if not os.path.exists("train_split" + "2"):
        os.mkdir("train_split" + "2")
for i in list_2:
    src_path = train_dir + i + ".png"
    dst_path = "train_split" + "2" + "/" + i + ".png"
    shutil.copy(src_path, dst_path)
    
    
 train_dir = "train_image/"
    # Create subdirectory with `class_name`
if not os.path.exists("train_split" + "1"):
        os.mkdir("train_split" + "1")
for i in list_1:
    src_path = train_dir + i + ".png"
    dst_path = "train_split" + "1" + "/" + i + ".png"
    shutil.copy(src_path, dst_path)
    
    
train_dir = "train_image/"
    # Create subdirectory with `class_name`
if not os.path.exists("train_split" + "0"):
        os.mkdir("train_split" + "0")
for i in list_0:
    src_path = train_dir + i + ".png"
    dst_path = "train_split" + "0" + "/" + i + ".png"
    shutil.copy(src_path, dst_path)
    
    
import split_folders
input='dataset'
output='final_dataset'
split_folders.ratio(input, output=output, seed=1337, ratio=(.8, .1, .1))    
