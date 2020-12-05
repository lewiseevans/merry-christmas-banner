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

    # Tree trunk
    unicornhathd.set_pixel(7, 1, 139, 69, 19)
    unicornhathd.set_pixel(8, 1, 139, 69, 19)
    unicornhathd.set_pixel(7, 2, 139, 69, 19)
    unicornhathd.set_pixel(8, 2, 139, 69, 19)

    # Bottom row baubles
    unicornhathd.set_pixel(4, 2, 51, 0, 101)
    unicornhathd.set_pixel(6, 2, 0, 51, 51)
    unicornhathd.set_pixel(9, 2, 255, 0, 0)
    unicornhathd.set_pixel(11, 2, 255, 255, 0)

    # Bottom tree rows
    unicornhathd.set_pixel(4, 3, 0, 255, 0)
    unicornhathd.set_pixel(5, 3, 0, 255, 0)
    unicornhathd.set_pixel(6, 3, 0, 255, 0)
    unicornhathd.set_pixel(7, 3, 0, 255, 0)
    unicornhathd.set_pixel(8, 3, 0, 255, 0)
    unicornhathd.set_pixel(9, 3, 0, 255, 0)
    unicornhathd.set_pixel(10, 3, 0, 255, 0)
    unicornhathd.set_pixel(11, 3, 0, 255, 0)

    unicornhathd.set_pixel(5, 4, 0, 255, 0)
    unicornhathd.set_pixel(6, 4, 0, 255, 0)
    unicornhathd.set_pixel(7, 4, 0, 0, 255)
    unicornhathd.set_pixel(8, 4, 0, 255, 0)
    unicornhathd.set_pixel(9, 4, 0, 255, 0)
    unicornhathd.set_pixel(10, 4, 0, 255, 0)

    unicornhathd.set_pixel(6, 5, 0, 255, 0)
    unicornhathd.set_pixel(7, 5, 0, 255, 0)
    unicornhathd.set_pixel(8, 5, 0, 255, 0)
    unicornhathd.set_pixel(9, 5, 0, 255, 0)

    unicornhathd.set_pixel(5, 5, 102, 0, 204)
    unicornhathd.set_pixel(7, 5, 0, 255, 0)
    unicornhathd.set_pixel(8, 5, 0, 255, 0)
    unicornhathd.set_pixel(10, 5, 0, 0, 255)

    # Show the image
    unicornhathd.show()

    time.sleep(5)
