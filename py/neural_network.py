#!/usr/bin/env python
import cv2
import numpy as np

from config_reader import ConfigReader

__author__ = "Lukasz Wierzbicki"
__version__ = "1.0.0"
__maintainer__ = "Lukasz Wierzbicki"
__email__ = "01113202@pw.edu.pl"


class NeuralNetwork:
    """
    CNN neural network used to colorize grayscale image.
    [https://arxiv.org/pdf/1603.08511]
    ...

    Attributes
    ----------
    __PROTO_FILE
        file with cnn description. Describe the structure of neural network

    __WEIGHTS_FILE
        file that defines the internal parameters of cnn layers.

    __QUANTIZED_LAB_SPACE
        file with quantized lab space.

    __INPUT_WIDTH
        cnn input width.

    __INPUT_HEIGHT
        cnn input height.

    __neural_network
        instance of cnn neural network

    Methods
    -------
    populate(blob_matrix)
        sets input (blob_matrix) of __neural_network instance.

    predict_ab_space()
        predicts the ab space based on the provided input with the method populate()
    """

    def __init__(self):
        config_reader = ConfigReader()
        self.__PROTO_FILE = config_reader.get_string_property('ProtoFile')
        self.__WEIGHTS_FILE = config_reader.get_string_property('WeightsFile')
        quantized_lab_space_path = config_reader.get_string_property('QuantizedLabSpace')
        self.__QUANTIZED_LAB_SPACE = np.load(quantized_lab_space_path).transpose().reshape(2, 313, 1, 1)
        self.__INPUT_WIDTH = config_reader.get_int_property('Width')
        self.__INPUT_HEIGHT = config_reader.get_int_property('Height')

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
