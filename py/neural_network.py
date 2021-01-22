#!/usr/bin/env python
import numpy as np
import cv2

__author__ = "Lukasz Wierzbicki"
__version__ = "1.0.0"
__maintainer__ = "Lukasz Wierzbicki"
__email__ = "01113202@pw.edu.pl"


class NeuralNetwork:
    def __init__(self):
        self.__PROTO_FILE = '../models/colorization_deploy_v2.prototxt'
        self.__WEIGHTS_FILE = '../models/colorization_release_v2.caffemodel'
        self.__QUANTIZED_LAB_SPACE = np.load('../models/quantized_lab_space.npy').transpose().reshape(2, 313, 1, 1)
        self.__INPUT_WIDTH = 224
        self.__INPUT_HEIGHT = 224

        self.__neural_network = cv2.dnn.readNetFromCaffe(self.__PROTO_FILE, self.__WEIGHTS_FILE)
        self.__populate_network_layers_with_quantized_lab_space()

    def __populate_network_layers_with_quantized_lab_space(self):
        # populate cluster centers as 1x1 convolution kernel. Based on 'colorization_deploy_v2.prototxt'
        class8 = self.__neural_network.getLayerId("class8_ab")
        conv8 = self.__neural_network.getLayerId("conv8_313_rh")
        self.__neural_network.getLayer(class8).blobs = [self.__QUANTIZED_LAB_SPACE.astype("float32")]
        self.__neural_network.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

    def predict_ab_space(self):
        result = self.__neural_network.forward()
        return result[0, :, :, :].transpose((1, 2, 0))

    def populate(self, blob_matrix):
        self.__neural_network.setInput(blob_matrix)

    def get_width(self):
        return self.__INPUT_WIDTH

    def get_height(self):
        return self.__INPUT_HEIGHT
