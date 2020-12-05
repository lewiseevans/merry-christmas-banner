#!/usr/bin/env python

import colorsys
import time
from sys import exit

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    exit('This script requires the pillow module\nInstall with: sudo pip install pillow')

import unicornhathd

print("Simple program to display Merry Christmas on a 16x16 colourful display")

TEXT = 'Merry Christmas Theo! Merry Christmas Maria! Merry Christmas Owen!'

FONT = ('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 10)

width, height = unicornhathd.get_shape()
unicornhathd.rotation(90)

text_x = 1
text_y = 2

font_file, font_size = FONT

font = ImageFont.truetype(font_file, font_size)

text_width, text_height = font.getsize(TEXT)

text_width += width + text_x

image = Image.new('RGB', (text_width, max(height, text_height)), (0, 0, 0))

draw = ImageDraw.Draw(image)

draw.text((text_x, text_y), TEXT, fill=(255, 255, 255), font=font)

for scroll in range(text_width - width):
    for x in range(width):

        hue = (x + scroll) / float(text_width)
        br, bg, bb = [int(n * 255) for n in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
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

unicornhathd.off()
