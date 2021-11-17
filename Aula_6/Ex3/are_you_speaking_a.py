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

    # Load the cascade
    # path_to_classifier =
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

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

        # ----------------------------------------------------------------------
        # face detection
        # ----------------------------------------------------------------------
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Converte para gray
        faces = face_cascade.detectMultiScale(image_gray, 1.1, 4)  # Detect faces

        for (x, y, w, h) in faces:  # Draw the rectangle around the face
            cv2.rectangle(image_gui, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw a Blue rectangle aroound face

            mask_face = np.ndarray((heigth, width), dtype=np.uint8)  # create a mask same size as image
            mask_face.fill(0)  # set image to all zeros
            mask_face = cv2.rectangle(mask_face, (x, y), (x + w, y + h), 255, -1)  # draw blue recttangle around face

            cv2.add(image, (-10, 58, -10, 0), dst=image_gui, mask=mask_face)  # paint face color green
            cv2.imshow('new mask_face', mask_face)

        # cv2.add(image,(-10,50,-10,0),dst=image_gui,mask=mask_face) #paint face color green
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
