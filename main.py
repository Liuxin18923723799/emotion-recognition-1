#!/usr/bin/env python

###############################################################################
# OpenCV + Caffe
# Uses OpenCV for face detection and cropping to serve as inputs to Caffe.
# Uses a Caffe VGG_S net from EmotiW'15 [1] to classify emotion.
# Authors: Gautam Shine, Dan Duncan
#
# [1] Gil Levi and Tal Hassner, Emotion Recognition in the Wild via
# Convolutional Neural Networks and Mapped Binary Patterns, Proc. ACM
# International Conference on Multimodal Interaction (ICMI), Seattle, Nov. 2015
###############################################################################

import os, shutil, sys, time, re, glob
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from PIL import Image
import caffe

from caffe_functions import *
from opencv_functions import *
from utility_functions import *

### USER-SPECIFIED VARIABLES: ###

# List your dataset root directories here:
dirJaffe = 'datasets/jaffe'
dirCKPlus = 'datasets/CK_Plus'
dirMisc = 'datasets/misc'
dirTraining = 'datasets/validation_images'

# Select which dataset to use (case insensitive):
dataset = 'jaffe'
#dataset = 'ckplus'
#dataset = 'training'
#dataset = 'misc'

# Flags:
cropFlag = True # False disables image cropping
plot_confusion = True
useMean = False # Use image mean during classification

### START SCRIPT: ###

# Set up inputs
dir = None
if dataset.lower() == 'jaffe':
    dir = dirJaffe
    color = False
    single_face = True
    cropFlag = True
    useMean = True
elif dataset.lower() == 'ckplus':
    dir = dirCKPlus
    color = False
    single_face = True
    cropFlag = True
    useMean = True
elif dataset.lower() == 'misc':
    dir = dirMisc
    color = True
    single_face = False
elif dataset.lower() == 'training':
    dir = dirTraining
    color = True
    single_face = True
    cropFlag = False
    useMean = True
else:
    print('Error - Unsupported dataset: ' + dataset)
    sys.exit(0)

# Clean up and discard anything from the last run
dirCrop = dir + '/cropped'
rmdir(dirCrop)

# Master list of categories for EmotitW network
categories = ['Angry' , 'Disgust' , 'Fear' , 'Happy'  , 'Neutral' ,  'Sad' , 'Surprise']

# Start keeping time:
t0 = time.time()

# Load dataset image list
input_list, labels = importDataset(dir, dataset, categories)

# Perform detection and cropping if desired (and it should be desired)
crop_time = None
if cropFlag:
    start = time.time()
    mkdir(dirCrop)
    input_list = faceCrop(dirCrop, input_list, color, single_face)
    crop_time = time.time() - start


# Perform classification
start = time.time()
classify_emotions(input_list, color, categories, labels, plot_neurons=False, plot_confusion=plot_confusion, useMean=useMean)
classify_time = time.time() - start
totalTime = time.time() - t0

print('\nNumber of images: ' + str(len(input_list)))
if crop_time is not None:
    print('Crop time: ' + str(crop_time) + 's\t(' + str(crop_time / len(input_list)) + "s / image)")
print('Classify time: ' + str(classify_time) + 's\t(' + str(classify_time / len(input_list)) + "s / image)")
print('Total time: ' + str(totalTime) + 's\t(' + str(totalTime / len(input_list)) + "s / image)")
