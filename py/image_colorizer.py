#!/usr/bin/env python
import cv2

from abstract_colorizer import AbstractColorizer

__author__ = "Lukasz Wierzbicki"
__version__ = "1.0.0"
__maintainer__ = "Lukasz Wierzbicki"
__email__ = "01113202@pw.edu.pl"


class ImageColorizer(AbstractColorizer):
    """
    A class used to represent an Image implementation of abstract colorizer.
    The image file provides the input data to colorization algorithm.

    ...

    Attributes
    ----------
    __destination:
        path to the colored file

    __bgr_image:
        image in BGR space to colorize

    Methods
    -------
    colorize()
        Colorizes grayscale image and store it.
    """

    def __init__(self, source, destination):
        super().__init__()
        self.__destination = destination
        self.__bgr_image = source

    def colorize(self):
        result = self._colorization_solver.solve(self.__bgr_image)
        self.__store_result(result)

    def __store_result(self, result):
        cv2.imwrite(self.__destination, result)
