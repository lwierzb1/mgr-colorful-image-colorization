#!/usr/bin/env python
"""General purpose functions useful for image processing.
"""

import cv2
import numpy as np

__author__ = "Lukasz Wierzbicki"
__version__ = "1.0.0"
__maintainer__ = "Lukasz Wierzbicki"
__email__ = "01113202@pw.edu.pl"


def read_as_float_matrix(path):
    """Returns float matrix representation of image specified with path.
    Normalization will help to remove distortions caused by lights and shadows in an image.

    path: Path to image. data. It can be absolute or relative.
    """

    bgr_image = cv2.imread(path)
    return bgr_image_to_float_matrix(bgr_image)


def bgr_image_to_float_matrix(bgr_image):
    return bgr_image.astype(np.float32) / 255.


def bgr_to_lab_channels(matrix):
    """Returns Lab space channels representation of matrix in BGR space.

    matrix: matrix of float in BGR color space.
    """
    lab_matrix = cv2.cvtColor(matrix, cv2.COLOR_BGR2LAB)
    return cv2.split(lab_matrix)


def lab_matrix_to_rgb_image(lab_matrix):
    """Returns image in RGB space representation based on CIELab space matrix.

    matrix: CIELab matrix
    """
    rgb_matrix = cv2.cvtColor(lab_matrix, cv2.COLOR_LAB2BGR)
    # clip any values that fall outside the range [0, 1]
    rgb_matrix = np.clip(rgb_matrix, 0, 1)

    # the current colorized image is represented as a floating point
    # data type in the range [0, 1] -- let's convert to an unsigned
    # 8-bit integer representation in the range [0, 255]
    colorized_rgb_image = (255 * rgb_matrix).astype("uint8")
    return colorized_rgb_image


def resize_matrix(matrix, width, height):
    """Resizes matrix to given width and height.
    """
    return cv2.resize(matrix, (width, height))


def merge_l_channel_with_ab_space(l_channel, ab_space):
    l_channel_matrix = l_channel[:, :, np.newaxis]
    return np.concatenate((l_channel_matrix, ab_space), axis=2)


def matrix_to_blob(matrix):
    """Returns blob representation of image matrix.
    """
    return cv2.dnn.blobFromImage(matrix)


def rgb_matrix_to_image(matrix):
    """Returns rgb image representation of float matrix.

    matrix: float matrix.
    """

    rgb_image = (matrix * 255).astype(np.int)
    return rgb_image
