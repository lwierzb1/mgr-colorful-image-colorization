#!/usr/bin/env python
"""A Python implementation of Colorful Image Colorization
  This code is based on
  Richard Zhang, Phillip Isola and Alexei A. Efros
  "Colorful Image Colorization."
  https://richzhang.github.io/colorization/
Example usage:
  $ python main.py --input bw.bmp --mode image --store colored.bmp
"""
import argparse
import os
import time
import statistics
from camera_colorizer import CameraColorizer
from image_colorizer import ImageColorizer
from video_colorizer import VideoColorizer

__author__ = "Lukasz Wierzbicki"
__version__ = "1.0.0"
__maintainer__ = "Lukasz Wierzbicki"
__email__ = "01113202@pw.edu.pl"


def parse_args():
    # parse command line arguments
    parser = argparse.ArgumentParser(description='Colorful Image Colorization')
    parser.add_argument('--input', help='grayscale image')
    parser.add_argument('--mode', choices=['image', 'video', 'camera'], help='Special testing value')
    parser.add_argument('--store', help='path to store result of algorithm')
    args = parser.parse_args()

    if args.mode == 'image' or args.mode == 'video':
        if args.input is None:
            print('Please give the input greyscale image name.')
            exit()

        if os.path.isfile(args.input) == 0:
            print('Input file does not exist')
            exit()

        if args.store is None:
            print('Please give the store path.')
            exit()
    return args


def create_colorizer(args):
    if args.mode == 'image':
        return ImageColorizer(args.input, args.store)
    elif args.mode == 'video':
        return VideoColorizer(args.input, args.store)
    else:
        return CameraColorizer()


def main():
    args = parse_args()
    xd = []
    for i in range(10):
        start = time.time()
        colorizer = create_colorizer(args)
        colorizer.colorize()
        end = time.time()
        xd.append(end - start)
    print(min(xd), statistics.mean(xd), max(xd))


if __name__ == "__main__":
    main()
