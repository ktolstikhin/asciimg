#!/usr/bin/env python3
"""asciimg - convert image into ASCII text.
"""
import sys
import argparse

import asciimg
from asciimg.draw import img_to_ascii
from asciimg.print import img_print


def get_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('image', help='image file')
    parser.add_argument('-w', '--width', type=int, default=79,
                        help='ascii width (char)')
    parser.add_argument('-p', '--print', action='store_true',
                        help='plot the resulting ascii text')
    parser.add_argument('-v', '--version', action='version',
                        version=asciimg.__version__,
                        help='show the version number and exit')
    args = parser.parse_args()
    return args


def main():
    args = get_args()

    try:
        img_ascii = img_to_ascii(args.image, args.width)
    except FileNotFoundError as e:
        print('Error: {}'.format(e), file=sys.stderr)
        sys.exit(-1)

    print(img_ascii)


if __name__ == '__main__':
    main()

