#!/usr/bin/env python3
import argparse
import copy
from functools import partial

import cv2
import numpy as np
import functools

image_gray = None
image = None
window_name = 'window - Ex3a'

ranges = {'b': {'min': 0, 'max': 256},
          'g': {'min': 0, 'max': 256},
          'r': {'min': 0, 'max': 256}}

def segmentor():
    global image, ranges

    # Processing
    mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']])
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    mask = cv2.inRange(image, mins, maxs)
    mask = mask.astype(np.bool)

    image_processed = copy.deepcopy(image)
    image_processed [np.logical_not(mask)]=0

    cv2.imshow(window_name, image_processed)

def onTrackbar(value,channel,min_max):
    global ranges
    ranges[channel][min_max]=value
    segmentor()


def main():

    global image
    image_filename1 = '/home/analtino/Desktop/psr/PRS_Pessoal/Aula_5/Imagens/atlas2000_e_atlasmv.png'  # 'path to my image .png'
    image = cv2.imread(image_filename1, cv2.IMREAD_COLOR)  # Load an image

    global image_gray
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    #image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image

    cv2.namedWindow(window_name)


    # add code to create the trackbar ...
    trackbar_name = 'Treshold'

    #partial function
    myonTrackbar = partial(onTrackbar, image_gray =image_gray, window_name=window_name)


    cv2.createTrackbar('MinB', window_name, 0, 256,partial(onTrackbar, channel='b',min_max='min'))
    cv2.createTrackbar('MaxB', window_name, 256, 256, partial(onTrackbar, channel='b', min_max='max'))
    cv2.createTrackbar('MinG', window_name, 0, 256, partial(onTrackbar, channel='g', min_max='min'))
    cv2.createTrackbar('MaxG', window_name, 256, 256, partial(onTrackbar, channel='g', min_max='max'))
    cv2.createTrackbar('MinR', window_name, 0, 256, partial(onTrackbar, channel='r', min_max='min'))
    cv2.createTrackbar('MaxR', window_name, 256, 256, partial(onTrackbar, channel='r', min_max='max'))


    #onTrackbar(128)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()