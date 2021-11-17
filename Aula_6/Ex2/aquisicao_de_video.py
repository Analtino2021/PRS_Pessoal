#!/usr/bin/env python3
import copy

import cv2
import numpy as np


def main():
    # -----------------------------------------------------------------------
    # initialization
    # -----------------------------------------------------------------------
    capture = cv2.VideoCapture(0)
    # configure opencv window
    window_name = 'A5-Ex3'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    # -----------------------------------------------------------------------
    # Execution
    # -----------------------------------------------------------------------
    while True:
        _, image = capture.read()  # get image from camera
        if image is None:
            print('Video is over, terminating.')
            break  # video is over

        heigth, width, _ = image.shape  # tamanho da minha imagem
        image_gui = copy.deepcopy(image)

        cv2.imshow(window_name, image_gui)
        key = cv2.waitKey(113)

        # ----------------------------------------------------------------------
        # TERMINATION
        # ----------------------------------------------------------------------
        if key == ord('q'):  # q for quit
            print("you Pressed q... aborting")
            break


if __name__ == '__main__':
    main()
