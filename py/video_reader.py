#!/usr/bin/env python
import cv2

__author__ = "Lukasz Wierzbicki"
__version__ = "1.0.0"
__maintainer__ = "Lukasz Wierzbicki"
__email__ = "01113202@pw.edu.pl"


class VideoReader:
    """
    A class used to represent an Video reader.
    An object of this class has the functionality of loading frames from video file.

    ...

    Attributes
    ----------
    __video_stream:
        stream that has access to the frames of video

    __WIDTH:
       width of video [px]

    __HEIGHT:
        height of video [px]
    Methods
    -------
    read_next_frame()
        reads next frame from video.

    get_video_shape()
        returns width and height of video being read
    """

    def __init__(self, source_path):
        self.__video_stream = cv2.VideoCapture(source_path)
        self.__WIDTH = self.__video_stream.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.__HEIGHT = self.__video_stream.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def read_next_frame(self):
        frame = self.__video_stream.read()
        return frame

    def get_video_shape(self):
        return int(self.__WIDTH), int(self.__HEIGHT)
