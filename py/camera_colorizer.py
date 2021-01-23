#!/usr/bin/env python
import cv2
import numpy as np

from abstract_colorizer import AbstractColorizer

__author__ = "Lukasz Wierzbicki"
__version__ = "1.0.0"
__maintainer__ = "Lukasz Wierzbicki"
__email__ = "01113202@pw.edu.pl"


class CameraColorizer(AbstractColorizer):
    """
    A class used to represent an Camera implementation of abstract colorizer.
    The camera provides the input data to colorization algorithm.

    ...

    Attributes
    ----------
    __camera
        an object that has access to the camera image

    Methods
    -------
    colorize()
        Colorizes grayscale frame from camera.
    """

    def __init__(self):
        super().__init__()
        self.__camera = cv2.VideoCapture(0)

    def colorize(self):
        while True:
            # Capture frame-by-frame
            frame_exists, frame = self.__camera.read()

            if frame_exists is False:
                break
            else:
                colored = self._colorization_solver.solve(frame)
                show_result(frame, colored)
                k = cv2.waitKey(33)
                if k == 27:  # Esc key to stop
                    break

    def __del__(self):
        self.__camera.release()
        cv2.destroyAllWindows()


def show_result(original, colored):
    compare_matrix = np.concatenate((original, colored), axis=1)
    # Display the resulting frame
    cv2.imshow('Result', compare_matrix)
