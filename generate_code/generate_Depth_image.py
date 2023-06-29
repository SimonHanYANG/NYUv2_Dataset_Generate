"""
Author: SimonHanYANG SimonCK666@mail.163.com
Date: 2023-06-29 11:19:34
LastEditors: SimonHanYANG SimonCK666@mail.163.com
LastEditTime: 2023-06-29 11:19:42
FilePath: \generate_code\generate_Depth_image.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
"""
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import numpy as np
import h5py
import os
from PIL import Image

f = h5py.File("D:\\NYUv2\\nyu_depth_v2_labeled.mat")

depths = f["depths"]
depths = np.array(depths)

path_converted = "../nyu_depths/"
if not os.path.isdir(path_converted):
    os.makedirs(path_converted)

max = depths.max()
print(depths.shape)
print(depths.max())
print(depths.min())

depths = depths / max * 255
depths = depths.transpose((0, 2, 1))

print(depths.max())
print(depths.min())

for i in range(len(depths)):
    print(str(i) + ".png" + " DONE...")
    depths_img = Image.fromarray(np.uint8(depths[i]))
    depths_img = depths_img.transpose(Image.FLIP_LEFT_RIGHT)
    iconpath = path_converted + str(i) + ".png"
    depths_img.save(iconpath, "PNG", optimize=True)
