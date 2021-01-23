#!/usr/bin/env python
from image_processing_toolkit import *
from neural_network import NeuralNetwork

__author__ = "Lukasz Wierzbicki"
__version__ = "1.0.0"
__maintainer__ = "Lukasz Wierzbicki"
__email__ = "01113202@pw.edu.pl"


class ColorizationSolver:
    """
    A class used to solve Colorization problem. Using CNN [https://en.wikipedia.org/wiki/Convolutional_neural_network]
    to colorize image. Gets grayscale image in BGR space, returns colorized image in BGR space.

    Attributes
    ----------
    __neural_network
        instance of CNN neural network

    Methods
    -------
    solve()
        Colorizes input grayscale image using CNN.
    """

    def __init__(self):
        self.__neural_network = NeuralNetwork()

    def solve(self, grayscale_bgr_image):
        grayscale_bgr_matrix = bgr_image_to_float_matrix(grayscale_bgr_image)

        image_width = grayscale_bgr_matrix.shape[1]
        image_height = grayscale_bgr_matrix.shape[0]

        l_channel, _, _ = bgr_to_lab_channels(grayscale_bgr_matrix)
        predicted_ab_space = self.__predicate_ab_space(l_channel)
        ab_space = resize_matrix(predicted_ab_space, image_width, image_height)
        colorized_lab_matrix = merge_l_channel_with_ab_space(l_channel, ab_space)
        colorized_bgr_image = lab_matrix_to_bgr_image(colorized_lab_matrix)
        return colorized_bgr_image

    def __predicate_ab_space(self, l_channel):
        resized_l_channel = resize_matrix(l_channel, self.__neural_network.get_width(),
                                          self.__neural_network.get_height())
        # l_channel is 0-100 to speed later mathematical process we can center it in 0
        resized_l_channel -= 50
        blob_l_channel = matrix_to_blob(resized_l_channel)
        self.__neural_network.populate(blob_l_channel)
        predicted_ab_space = self.__neural_network.predict_ab_space()
        return predicted_ab_space
