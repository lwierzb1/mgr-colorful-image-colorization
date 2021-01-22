#!/usr/bin/env python
import cv2

__author__ = "Lukasz Wierzbicki"
__version__ = "1.0.0"
__maintainer__ = "Lukasz Wierzbicki"
__email__ = "01113202@pw.edu.pl"


class VideoWriter:
    """
       A class used to represent an Video reader.
       An object of this class has the functionality of saving frames to video file.

       ...

       Attributes
       ----------
       __FPS:
           number of frames per second

       __SIZE:
          size of video (width, height)

       __video_writer:
           writes frames as video
       Methods
       -------
       write_frame(frame)
           writes frame as part of video
       """

    def __init__(self, store_path, size):
        self.__FPS = 25.0
        self.__SIZE = size
        self.__FOURCC = cv2.VideoWriter_fourcc(*'DIVX')

        self.__video_writer = cv2.VideoWriter(store_path, self.__FOURCC, self.__FPS, self.__SIZE)

    def write_frame(self, frame):
        self.__video_writer.write(frame)

    def __del__(self):
        self.__video_writer.release()
