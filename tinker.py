# bmp -> hd5 (for caffe)

import os
import sys
import numpy as np
import h5py

sys.path.append('$CAFFE_HOME/opencv-2.4.13/release/lib/')
import cv2

# Parameters
scale = 3
stride = 19
size_ground = 19
size_input = 7
size_pad = 2

#Read image to process
image = cv2.imread('<PATH TO FILES>/Train/t1.bmp')

#Change color-space to YCR_CB
image_ycrcb = cv2.cvtColor(image, cv2.COLOR_RGB2YCR_CB)
image_ycrcb = image_ycrcb[:,:,0]
image_ycrcb = image_ycrcb.reshape((image_ycrcb.shape[0], image_ycrcb.shape[1], 1))

#Compute size of LR images and resize HR images to a multiple of scale
height_small = int(height/scale)
width_small  = int(width/scale)

image_pair_HR = cv2.resize(image_ycrcb, (width_small*scale, height_small*scale) )
image_pair_LR = cv2.resize(image_ycrcb, (width_small, height_small) )

# Declare tensors to hold 1024 LR-HR subimage pairs
input_HR = np.zeros((size_ground, size_ground, 1, 1024))
input_LR = np.zeros((size_input + 2*size_pad, size_input + 2*size_pad, 1, 1024))

height, width = image_pair_HR.shape[:2]

#Iterate over the train image using the specified stride and create LR-HR subimage pairs
count = 0
for i in range(0, height-size_ground+1, stride):
    for j in range(0, width-size_ground+1, stride):
       subimage_HR = image_pair_HR[i:i+size_ground, j:j+size_ground]
       count = count + 1
       height_small = size_input
       width_small  = size_input
       subimage_LR = cv2.resize(subimage_HR, (width_small, height_small) )

       np.lib.pad(subimage_LR, ((size_pad, 2), (2, 2)), 'constant', constant_values=(0.0))
       input_HR[:,:,0,count-1] = subimage_HR
       input_LR[:,:,0,count-1] = np.lib.pad(subimage_LR, ((size_pad, 2), (2, 2)), 'constant', constant_values=(0.0))
