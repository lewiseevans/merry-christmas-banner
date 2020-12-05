#!/usr/bin/env python

import unicornhathd
import time

# Get the width and height of the display
width, height = unicornhathd.get_shape()


def draw():

    # Clear the display
    unicornhathd.off()

    # Clear the buffer
    unicornhathd.clear()

    # Set the rotation of the display
    unicornhathd.rotation(270)

    time.sleep(0.5)

    unicornhathd.set_pixel(6, 1, 255, 255, 255)
    unicornhathd.set_pixel(7, 1, 255, 255, 255)
    unicornhathd.set_pixel(8, 1, 255, 255, 255)
    unicornhathd.set_pixel(9, 1, 255, 255, 255)

    unicornhathd.set_pixel(5, 2, 255, 255, 255)
    unicornhathd.set_pixel(6, 2, 255, 255, 255)
    unicornhathd.set_pixel(7, 2, 255, 255, 255)
    unicornhathd.set_pixel(8, 2, 255, 255, 255)
    unicornhathd.set_pixel(9, 2, 255, 255, 255)
    unicornhathd.set_pixel(10, 2, 255, 255, 255)

    unicornhathd.set_pixel(5, 3, 255, 255, 255)
    unicornhathd.set_pixel(6, 3, 255, 255, 255)
    unicornhathd.set_pixel(7, 3, 255, 255, 255)
    unicornhathd.set_pixel(8, 3, 255, 255, 255)
    unicornhathd.set_pixel(9, 3, 255, 255, 255)
    unicornhathd.set_pixel(10, 3, 255, 255, 255)

    unicornhathd.set_pixel(5, 4, 255, 255, 255)
    unicornhathd.set_pixel(6, 4, 255, 255, 255)
    unicornhathd.set_pixel(9, 4, 255, 255, 255)
    unicornhathd.set_pixel(10, 4, 255, 255, 255)

    unicornhathd.set_pixel(5, 5, 255, 255, 255)
    unicornhathd.set_pixel(6, 5, 255, 255, 255)
    unicornhathd.set_pixel(7, 5, 255, 255, 255)
    unicornhathd.set_pixel(8, 5, 255, 255, 255)
    unicornhathd.set_pixel(9, 5, 255, 255, 255)
    unicornhathd.set_pixel(10, 5, 255, 255, 255)

    unicornhathd.set_pixel(5, 6, 255, 255, 255)
    unicornhathd.set_pixel(6, 6, 255, 204, 229)
    unicornhathd.set_pixel(7, 6, 255, 204, 229)
    unicornhathd.set_pixel(8, 6, 255, 204, 229)
    unicornhathd.set_pixel(9, 6, 255, 204, 229)
    unicornhathd.set_pixel(10, 6, 255, 255, 255)

    unicornhathd.set_pixel(5, 7, 255, 255, 255)
    unicornhathd.set_pixel(7, 7, 255, 204, 229)
    unicornhathd.set_pixel(8, 7, 255, 204, 229)
    unicornhathd.set_pixel(10, 7, 255, 255, 255)

    unicornhathd.set_pixel(5, 8, 255, 255, 255)
    unicornhathd.set_pixel(6, 8, 255, 204, 229)
    unicornhathd.set_pixel(7, 8, 255, 204, 229)
    unicornhathd.set_pixel(8, 8, 255, 204, 229)
    unicornhathd.set_pixel(9, 8, 255, 204, 229)
    unicornhathd.set_pixel(10, 8, 255, 255, 255)

    unicornhathd.set_pixel(4, 9, 255, 255, 255)
    unicornhathd.set_pixel(5, 9, 255, 255, 255)
    unicornhathd.set_pixel(6, 9, 255, 255, 255)
    unicornhathd.set_pixel(7, 9, 255, 255, 255)
    unicornhathd.set_pixel(8, 9, 255, 255, 255)
    unicornhathd.set_pixel(9, 9, 255, 255, 255)
    unicornhathd.set_pixel(10, 9, 255, 255, 255)
    unicornhathd.set_pixel(11, 9, 255, 255, 255)

    unicornhathd.set_pixel(4, 10, 255, 255, 255)
    unicornhathd.set_pixel(5, 10, 255, 255, 255)
    unicornhathd.set_pixel(6, 10, 255, 255, 255)
    unicornhathd.set_pixel(7, 10, 255, 255, 255)
    unicornhathd.set_pixel(8, 10, 255, 255, 255)
    unicornhathd.set_pixel(9, 10, 255, 255, 255)
    unicornhathd.set_pixel(10, 10, 255, 255, 255)
    unicornhathd.set_pixel(11, 10, 255, 255, 255)

    unicornhathd.set_pixel(5, 11, 255, 0, 0)
    unicornhathd.set_pixel(6, 11, 255, 0, 0)
    unicornhathd.set_pixel(7, 11, 255, 0, 0)
    unicornhathd.set_pixel(8, 11, 255, 0, 0)
    unicornhathd.set_pixel(9, 11, 255, 0, 0)
    unicornhathd.set_pixel(10, 11, 255, 0, 0)

    unicornhathd.set_pixel(6, 12, 255, 0, 0)
    unicornhathd.set_pixel(7, 12, 255, 0, 0)
    unicornhathd.set_pixel(8, 12, 255, 0, 0)
    unicornhathd.set_pixel(9, 12, 255, 0, 0)

    unicornhathd.set_pixel(7, 13, 255, 0, 0)
    unicornhathd.set_pixel(8, 13, 255, 0, 0)
    unicornhathd.set_pixel(10, 13, 255, 255, 255)

    unicornhathd.set_pixel(8, 14, 255, 0, 0)
    unicornhathd.set_pixel(9, 14, 255, 0, 0)

    unicornhathd.show()

    time.sleep(5)
