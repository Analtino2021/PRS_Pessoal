#!/usr/bin/env python3
import argparse
import cv2

# Global variables
window_name = 'window - Ex3a'
#image_gray = None


def onTrackbar(threshold):
    # Add code here to threshold image_gray and show image in window
    _, image_processed = cv2.threshold(image_gray,threshold,255,cv2.THRESH_BINARY)
    cv2.imshow(window_name, image_processed)

def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    # args = vars(parser.parse_args())

    image_filename1 = '/home/analtino/Desktop/psr/PRS_Pessoal/Aula_5/Imagens/atlas2000_e_atlasmv.png'  # 'path to my image .png'
    image = cv2.imread(image_filename1, cv2.IMREAD_COLOR)  # Load an image
    #image = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image

    global image_gray # use global var
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    # add code to create the trackbar ...
    trackbar_name = 'Treshold'
    cv2.createTrackbar(trackbar_name, window_name, 0, 255, onTrackbar)

    onTrackbar(128)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()