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

    drawPurpleRow(2)
    drawPurpleRow(2)
    drawPurpleRow(3)
    drawPurpleRow(5)
    drawBlueRow(6)
    drawBlueRow(7)
    drawPurpleRow(8)
    drawPurpleRow(9)
    drawPurpleRow(10)
    drawPurpleRow(11)

    unicornhathd.show()

    time.sleep(5)


def drawBow():
    unicornhathd.set_pixel(3, 12, 102, 0, 204)
    unicornhathd.set_pixel(4, 12, 102, 0, 204)
    unicornhathd.set_pixel(5, 12, 102, 0, 204)
    unicornhathd.set_pixel(6, 12, 102, 0, 204)
    unicornhathd.set_pixel(7, 12, 102, 0, 204)
    unicornhathd.set_pixel(8, 12, 102, 0, 204)
    unicornhathd.set_pixel(9, 12, 102, 0, 204)
    unicornhathd.set_pixel(10, 12, 102, 0, 204)
    unicornhathd.set_pixel(11, 12, 102, 0, 204)
    unicornhathd.set_pixel(12, 12, 102, 0, 204)


def drawBlueRow(y):
    unicornhathd.set_pixel(2, y, 0, 0, 255)
    unicornhathd.set_pixel(3, y, 0, 0, 255)
    unicornhathd.set_pixel(4, y, 0, 0, 255)
    unicornhathd.set_pixel(5, y, 0, 0, 255)
    unicornhathd.set_pixel(6, y, 0, 0, 255)
    unicornhathd.set_pixel(7, y, 0, 0, 255)
    unicornhathd.set_pixel(8, y, 0, 0, 255)
    unicornhathd.set_pixel(9, y, 0, 0, 255)
    unicornhathd.set_pixel(10, y, 0, 0, 255)
    unicornhathd.set_pixel(11, y, 0, 0, 255)
    unicornhathd.set_pixel(12, y, 0, 0, 255)
    unicornhathd.set_pixel(13, y, 0, 0, 255)


def drawPurpleRow(y):
    unicornhathd.set_pixel(2, y, 102, 0, 204)
    unicornhathd.set_pixel(3, y, 102, 0, 204)
    unicornhathd.set_pixel(4, y, 102, 0, 204)
    unicornhathd.set_pixel(5, y, 102, 0, 204)
    unicornhathd.set_pixel(6, y, 102, 0, 204)
    unicornhathd.set_pixel(7, y, 0, 0, 255)
    unicornhathd.set_pixel(8, y, 0, 0, 255)
    unicornhathd.set_pixel(9, y, 102, 0, 204)
    unicornhathd.set_pixel(10, y, 102, 0, 204)
    unicornhathd.set_pixel(11, y, 102, 0, 204)
    unicornhathd.set_pixel(12, y, 102, 0, 204)
    unicornhathd.set_pixel(13, y, 102, 0, 204)
