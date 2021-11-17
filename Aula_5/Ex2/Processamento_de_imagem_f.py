#!/usr/bin/env python3
import argparse
import copy

import cv2
import numpy as np


def main():
    # Process arguments
    # parser = argparse.ArgumentParser(description='Opencv example')
    # parser.add_argument('--image1',type = str, help='Path to image')
    # args = vars(parser.parse_args())

    image_filename1 = '/home/analtino/Desktop/psr/PRS_Pessoal/Aula_5/Imagens/atlas2000_e_atlasmv.png'  # 'path to my image .png'
    image1 = cv2.imread(image_filename1, cv2.IMREAD_COLOR)  # Load an image

    # -----------------------------------------------------------------------
    # Execution
    # -----------------------------------------------------------------------
    while True:
        #Load image
        #image_rgb = cv2.imread(args['image1'], cv2.IMREAD_COLOR) #Load an image
        image_rgb =image1
        image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2HSV)
        ranges = {'h': {'min': 50, 'max': 70},
                  's': {'min': 100, 'max': 250},
                  'v': {'min': 50, 'max': 130}}

        # Processing
        mins = np.array([ranges['h']['min'], ranges['s']['min'], ranges['v']['min']])
        maxs = np.array([ranges['h']['max'], ranges['s']['max'], ranges['v']['max']])
        mask = cv2.inRange(image_hsv, mins, maxs)
        cv2.imshow('mask', mask)

        image_add = image_rgb.copy()
        cv2.add(image_add,(0,0,255,0),dst=image_add,mask=mask)

        '''
        #exit (0)
        # conversion from numpy from uint8 to bool
        mask = mask.astype(np.bool)

        image_processed = (copy.deepcopy(image_rgb))
        image_processed[np.logical_not(mask)] = (image_processed[np.logical_not(mask)] * 0.4).astype(np.uint8)
        cv2.imshow('not', image_processed)
        image_processed[mask] = (0, 0, 255)
        image_processed[mask] = (image_processed[mask] * 0.4).astype(np.uint8)

        print(type(image_rgb))
        print(image_rgb.shape)
        print(image_rgb.dtype)
        print(mask.dtype)
        print(image_processed.dtype)
        '''

        # Visualization
        #cv2.namedWindow('original', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('original', image_hsv)  # Display the image
        cv2.imshow('add', image_add)  # Display the image
        #cv2.imshow('mask', mask.astype(np.uint8) * 255)  # Display the image
        cv2.imshow('image_processed', mask)  # Display the image

        key = cv2.waitKey(113)

        # ----------------------------------------------------------------------
        # TERMINATION
        # ----------------------------------------------------------------------
        if key == ord('q'):  # q for quit
            print("you Pressed q... aborting")
            break

if __name__ == '__main__':
    main()