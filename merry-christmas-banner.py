#!/usr/bin/env python

import colorsys
import time
import sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit('This script requires the pillow module\nInstall with: sudo pip install pillow')

import unicornhathd
import signal


# Get the width and height of the display
width, height = unicornhathd.get_shape()

# Set the rotation of the display
unicornhathd.rotation(90)

# Select font and size
FONT = ('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 10)


def shutdownHandler(sig, frame):
    print('Shutting down')
    unicornhathd.off()
    sys.exit(0)


signal.signal(signal.SIGINT, shutdownHandler)


def drawStocking():

    # Clear the display
    unicornhathd.off()

    # Clear the buffer
    unicornhathd.clear()

    unicornhathd.set_pixel(4, 14, 255, 255, 255)
    unicornhathd.set_pixel(5, 14, 255, 255, 255)
    unicornhathd.set_pixel(6, 14, 255, 255, 255)
    unicornhathd.set_pixel(7, 14, 255, 255, 255)
    unicornhathd.set_pixel(8, 14, 255, 255, 255)
    unicornhathd.set_pixel(9, 14, 255, 255, 255)
    unicornhathd.set_pixel(10, 14, 255, 255, 255)
    unicornhathd.set_pixel(11, 14, 255, 255, 255)

    unicornhathd.set_pixel(4, 13, 255, 255, 255)
    unicornhathd.set_pixel(5, 13, 255, 255, 255)
    unicornhathd.set_pixel(6, 13, 255, 255, 255)
    unicornhathd.set_pixel(7, 13, 255, 255, 255)
    unicornhathd.set_pixel(8, 13, 255, 255, 255)
    unicornhathd.set_pixel(9, 13, 255, 255, 255)
    unicornhathd.set_pixel(10, 13, 255, 255, 255)
    unicornhathd.set_pixel(11, 13, 255, 255, 255)

    unicornhathd.set_pixel(5, 12, 255, 0, 0)
    unicornhathd.set_pixel(6, 12, 255, 0, 0)
    unicornhathd.set_pixel(7, 12, 255, 0, 0)
    unicornhathd.set_pixel(8, 12, 255, 0, 0)
    unicornhathd.set_pixel(9, 12, 255, 0, 0)
    unicornhathd.set_pixel(10, 12, 255, 0, 0)

    unicornhathd.set_pixel(5, 11, 255, 0, 0)
    unicornhathd.set_pixel(6, 11, 255, 0, 0)
    unicornhathd.set_pixel(7, 11, 255, 0, 0)
    unicornhathd.set_pixel(8, 11, 255, 0, 0)
    unicornhathd.set_pixel(9, 11, 255, 0, 0)
    unicornhathd.set_pixel(10, 11, 255, 0, 0)

    unicornhathd.set_pixel(5, 10, 255, 0, 0)
    unicornhathd.set_pixel(6, 10, 255, 0, 0)
    unicornhathd.set_pixel(7, 10, 255, 0, 0)
    unicornhathd.set_pixel(8, 10, 255, 0, 0)
    unicornhathd.set_pixel(9, 10, 255, 0, 0)
    unicornhathd.set_pixel(10, 10, 255, 0, 0)

    unicornhathd.set_pixel(5, 9, 255, 0, 0)
    unicornhathd.set_pixel(6, 9, 255, 0, 0)
    unicornhathd.set_pixel(7, 9, 255, 0, 0)
    unicornhathd.set_pixel(8, 9, 255, 0, 0)
    unicornhathd.set_pixel(9, 9, 255, 0, 0)
    unicornhathd.set_pixel(10, 9, 255, 0, 0)

    unicornhathd.set_pixel(5, 8, 255, 0, 0)
    unicornhathd.set_pixel(6, 8, 255, 0, 0)
    unicornhathd.set_pixel(7, 8, 255, 0, 0)
    unicornhathd.set_pixel(8, 8, 255, 0, 0)
    unicornhathd.set_pixel(9, 8, 255, 0, 0)
    unicornhathd.set_pixel(10, 8, 255, 0, 0)

    unicornhathd.set_pixel(5, 7, 255, 0, 0)
    unicornhathd.set_pixel(6, 7, 255, 0, 0)
    unicornhathd.set_pixel(7, 7, 255, 0, 0)
    unicornhathd.set_pixel(8, 7, 255, 0, 0)
    unicornhathd.set_pixel(9, 7, 255, 0, 0)
    unicornhathd.set_pixel(10, 7, 255, 0, 0)

    unicornhathd.set_pixel(5, 6, 255, 0, 0)
    unicornhathd.set_pixel(6, 6, 255, 0, 0)
    unicornhathd.set_pixel(7, 6, 255, 0, 0)
    unicornhathd.set_pixel(8, 6, 255, 0, 0)
    unicornhathd.set_pixel(9, 6, 255, 0, 0)
    unicornhathd.set_pixel(10, 6, 255, 0, 0)

    unicornhathd.set_pixel(4, 5, 255, 0, 0)
    unicornhathd.set_pixel(5, 5, 255, 0, 0)
    unicornhathd.set_pixel(6, 5, 255, 0, 0)
    unicornhathd.set_pixel(7, 5, 255, 0, 0)
    unicornhathd.set_pixel(8, 5, 255, 0, 0)
    unicornhathd.set_pixel(9, 5, 255, 0, 0)
    unicornhathd.set_pixel(10, 5, 255, 0, 0)

    unicornhathd.set_pixel(3, 4, 255, 0, 0)
    unicornhathd.set_pixel(4, 4, 255, 0, 0)
    unicornhathd.set_pixel(5, 4, 255, 0, 0)
    unicornhathd.set_pixel(6, 4, 255, 0, 0)
    unicornhathd.set_pixel(7, 4, 255, 0, 0)
    unicornhathd.set_pixel(8, 4, 255, 0, 0)
    unicornhathd.set_pixel(9, 4, 255, 0, 0)

    unicornhathd.set_pixel(3, 3, 255, 0, 0)
    unicornhathd.set_pixel(4, 3, 255, 0, 0)
    unicornhathd.set_pixel(5, 3, 255, 0, 0)
    unicornhathd.set_pixel(6, 3, 255, 0, 0)
    unicornhathd.set_pixel(7, 3, 255, 0, 0)
    unicornhathd.set_pixel(8, 3, 255, 0, 0)
    unicornhathd.set_pixel(9, 3, 255, 0, 0)

    unicornhathd.set_pixel(4, 2, 255, 0, 0)
    unicornhathd.set_pixel(5, 2, 255, 0, 0)
    unicornhathd.set_pixel(6, 2, 255, 0, 0)
    unicornhathd.set_pixel(7, 2, 255, 0, 0)
    unicornhathd.set_pixel(8, 2, 255, 0, 0)

    unicornhathd.show()

    time.sleep(5)


def rainbowBanner(text):

    # Clear the display
    unicornhathd.off()

    # Clear the buffer
    unicornhathd.clear()

    # We want to draw our text 1 pixel in, and 2 pixels down from the top left corner
    text_x = 1
    text_y = 2

    # Grab our font file and size as defined at the top of the script
    font_file, font_size = FONT

    # Load the font using PIL's ImageFont
    font = ImageFont.truetype(font_file, font_size)

    # Ask the loaded font how big our text will be
    text_width, text_height = font.getsize(text)

    # Make sure we accommodate enough width to account for our text_x left offset
    text_width += width + text_x

    # Now let's create a blank canvas wide enough to accomodate our text
    image = Image.new('RGB', (text_width, max(height, text_height)), (0, 0, 0))

    # To draw on our image, we must use PIL's ImageDraw
    draw = ImageDraw.Draw(image)

    # And now we can draw text at our desited (text_x, text_y) offset, using our loaded font
    draw.text((text_x, text_y), text, fill=(255, 255, 255), font=font)

    # To give an appearance of scrolling text, we move a 16x16 "window" across the image we generated above
    # The value "scroll" denotes how far this window is from the left of the image.
    # Since the window is "width" pixels wide (16 for UHHD) and we don't want it to run off the end of the,
    # image, we subtract "width".
    for scroll in range(text_width - width):
        for x in range(width):

            # Figure out what hue value we want at this point.
            # "x" is the position of the pixel on Unicorn HAT HD from 0 to 15
            # "scroll" is how far offset from the left of our text image we are
            # We want the text to be a complete cycle around the hue in the HSV colour space
            # so we divide the pixel's position (x + scroll) by the total width of the text
            # If this pixel were half way through the text, it would result in the number 0.5 (180 degrees)
            hue = (x + scroll) / float(text_width)

            # Now we need to convert our "hue" value into r,g,b since that's what colour space our
            # image is in, and also what Unicorn HAT HD understands.
            # This list comprehension is just a tidy way of converting the range 0.0 to 1.0
            # that hsv_to_rgb returns into integers in the range 0-255.
            # hsv_to_rgb returns a tuple of (r, g, b)
            br, bg, bb = [int(n * 255)
                          for n in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]

            # Since our rainbow runs from left to right along the x axis, we can calculate it once
            # for every vertical line on the display, and then re-use that value 16 times below:

            for y in range(height):
                # Get the r, g, b colour triplet from pixel x,y of our text image
                # Our text is white on a black background, so these will all be shades of black/grey/white
                # ie 255,255,255 or 0,0,0 or 128,128,128
                pixel = image.getpixel((x + scroll, y))

                # Now we want to turn the colour of our text - shades of grey remember - into a mask for our rainbow.
                # We do this by dividing it by 255, which converts it to the range 0.0 to 1.0
                r, g, b = [float(n / 255.0) for n in pixel]

                # We can now use our 0.0 to 1.0 range to scale our three colour values, controlling the amount
                # of rainbow that gets blended in.
                # 0.0 would blend no rainbow
                # 1.0 would blend 100% rainbow
                # and anything in between would copy the anti-aliased edges from our text
                r = int(br * r)
                g = int(bg * g)
                b = int(bb * b)

                # Finally we colour in our finished pixel on Unicorn HAT HD
                unicornhathd.set_pixel(width - 1 - x, y, r, g, b)

        # Finally, for each step in our scroll, we show the result on Unicorn HAT HD
        unicornhathd.show()

        # And sleep for a little bit, so it doesn't scroll too quickly!
        time.sleep(0.04)


THEO = 'Merry Christmas Theo!'
MARIA = 'Merry Christmas Maria!'
OWEN = 'Merry Christmas Owen!'

while True:
    drawStocking()
    # rainbowBanner(THEO)
    # rainbowBanner(MARIA)
    # rainbowBanner(OWEN)
