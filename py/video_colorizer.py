#!/usr/bin/env python
import cv2

from abstract_colorizer import AbstractColorizer
from video_reader import VideoReader
from video_writer import VideoWriter

__author__ = "Lukasz Wierzbicki"
__version__ = "1.0.0"
__maintainer__ = "Lukasz Wierzbicki"
__email__ = "01113202@pw.edu.pl"


class VideoColorizer(AbstractColorizer):
    """
    A class used to represent an Video implementation of abstract colorizer.
    The video file provides the input data to colorization algorithm.

    ...

    Attributes
    ----------
    __video_reader:
        an object that has ability to read frames from video files.

    __video_writer:
        an object that has ability to write frames as single video file.

    Methods
    -------
    colorize()
        Colorizes grayscale frame from video file.
    """

    def __init__(self, source, destination):
        super().__init__()
        self.__video_reader = VideoReader(source)
        self.__video_writer = VideoWriter(destination, self.__video_reader.get_video_shape())

    def colorize(self):
        while True:
            frame_exists, frame = self.__video_reader.read_next_frame()
            # if we are viewing a video and we did not grab a frame then we
            # have reached the end of the video
            if frame_exists is False:
                break
            colorized_frame = self._colorization_solver.solve(frame)
            self.__video_writer.write_frame(colorized_frame)
            key = cv2.waitKey()
            if key == 27:  # Esc key to stop
                break
