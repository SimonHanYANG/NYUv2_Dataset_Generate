"""
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-06-29 11:20:20
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-06-29 11:28:25
FilePath: \generate_code\generate_Lable.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
"""

# -*- coding: utf-8 -*-
import numpy as np
import h5py
import os
from PIL import Image

f = h5py.File("D:\\NYUv2\\nyu_depth_v2_labeled.mat")

labels = f["labels"]
labels = np.array(labels)

path_converted = "../nyu_labels/"
if not os.path.isdir(path_converted):
    os.makedirs(path_converted)

labels_number = []
for i in range(len(labels)):
    print(str(i) + ".png" + " DONE...")
    
    labels_number.append(labels[i])
    labels_0 = np.array(labels_number[i])
    label_img = Image.fromarray(np.uint8(labels_number[i]))
    label_img = label_img.transpose(Image.ROTATE_270)

    iconpath = "../nyu_labels/" + str(i) + ".png"
    label_img.save(iconpath, "PNG", optimize=True)
