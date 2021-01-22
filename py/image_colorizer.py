#!/usr/bin/env python
import cv2

from abstract_colorizer import AbstractColorizer
from image_processing_toolkit import read_as_float_matrix

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

    __grayscale_matrix:
        matrix of float to colorize

    Methods
    -------
    colorize()
        Colorizes grayscale image and store it.
    """

    def __init__(self, source, destination):
        super().__init__()
        self.__destination = destination
        self.__grayscale_matrix = read_as_float_matrix(source)

    def colorize(self):
        result = self._colorization_solver.solve(self.__grayscale_matrix)
        self.__store_result(result)

    def __store_result(self, result):
        cv2.imwrite(self.__destination, result)
