#!/usr/bin/env python3
import argparse

import cv2



#------------------------- 1a ---------------------------------------------
import numpy as np
from cv2 import FONT_ITALIC, LINE_8


def main():
    image_filename1 = '/home/analtino/Desktop/psr/PRS_Pessoal/Aula_5/Imagens/atlascar.png'  # 'path to my image .png'
    image1 = cv2.imread(image_filename1, cv2.IMREAD_COLOR) # Load an image

    height, width, _ = image1.shape
    print('width:  ', width)
    print('height: ', height)
    center_x=int(width/2)
    center_y=int(height/2)

    reference_x=int(width/4)
    cv2.circle(image1, (center_x,center_y), 150, (0, 0, 255), 5) # 1a
    cv2.putText(image1, 'ANALTINO',(reference_x,center_y),FONT_ITALIC,3 ,255,2,LINE_8)  #1b
    cv2.imshow('window', image1)  # Display the image
    cv2.waitKey(0)

if __name__ == '__main__':
    main()