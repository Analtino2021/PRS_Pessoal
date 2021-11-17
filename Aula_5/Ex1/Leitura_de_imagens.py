#!/usr/bin/env python3
import argparse

import cv2

def main():
    t=0
    # parser = argparse.ArgumentParser(description='Opencv EXAMPLE.')   #1B
    # parser.add_argument('--imagen1', type=str, help=' Path to image') #1B
    # args = vars(parser.parse_args())
    # print(args)
    #
    # image_filename = '/home/analtino/Transferências/kika1.jpg' #'path to my image .png'
    # #image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    # image = cv2.imread(args['imagen1'], cv2.IMREAD_COLOR)  # Load an image   #1C
    #
    # cv2.imshow('window', image)  # Display the image
    # cv2.waitKey(3000) # wait for a key press before proceeding

    #------------------------- 1C ---------------------------------------------
    while True:
        image_filename1 = '/home/analtino/Desktop/psr/PRS_Pessoal/Aula_5/Imagens/atlascar2.png'  # 'path to my image .png'
        image_filename2 = '/home/analtino/Desktop/psr/PRS_Pessoal/Aula_5/Imagens/atlascar.png'  # 'path to my image .png'
        image1 = cv2.imread(image_filename1, cv2.IMREAD_COLOR) # Load an image
        image2 = cv2.imread(image_filename2, cv2.IMREAD_COLOR) # Load an image

        remainder = t % 2
        print(remainder)
        if remainder == 0:
           t+=1
           cv2.imshow('window', image1)  # Display the image
           cv2.waitKey(3000)  # wait for a key press before proceeding
           k = cv2.waitKey(3000)
           #cv2.destroyWindow('window')
           #print(t)
        else:
           t+=1
           cv2.imshow('window', image2)  # Display the image
           cv2.waitKey(3000)  # wait for a key press before proceeding
           k=cv2.waitKey(3000)
           #cv2.destroyWindow('window')
           #print(t)
        if k == 27:
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()