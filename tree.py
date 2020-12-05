#!/usr/bin/env python

import unicornhathd
import time

# Get the width and height of the display
width, height = unicornhathd.get_shape()

# Set the rotation of the display
unicornhathd.rotation(270)


def drawTree():

    # Clear the display
    unicornhathd.off()

    # Clear the buffer
    unicornhathd.clear()

    unicornhathd.set_pixel(7, 1, 139, 69, 19)
    unicornhathd.set_pixel(7, 1, 139, 69, 19)
    unicornhathd.set_pixel(8, 2, 139, 69, 19)
    unicornhathd.set_pixel(8, 2, 139, 69, 19)

    # Show the image
    unicornhathd.show()

    time.sleep(5)
