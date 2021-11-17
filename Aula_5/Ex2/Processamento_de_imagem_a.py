#!/usr/bin/env python3
import argparse

import cv2

def main():
    # Process arguments
    parser = argparse.ArgumentParser(description='Opencv example')
    parser.add_argument('--image1',type = str, help='Path to image')
    args = vars(parser.parse_args())

    #Load image
    image_original = cv2.imread(args['image1'], cv2.IMREAD_COLOR) #Load an image
    image_gray = cv2.cvtColor(image_original,cv2.COLOR_BGR2GRAY)

    #Process image
    retval, image_processed = cv2.threshold(image_gray,128,255,cv2.THRESH_BINARY)

    # Visualization
    cv2.imshow('original', image_original)  # Display the image
    cv2.imshow('GRAY', image_gray)  # Display the image
    cv2.imshow('processed', image_processed)  # Display the image

    cv2.waitKey(8000)

if __name__ == '__main__':
    main()