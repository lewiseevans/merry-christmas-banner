#!/usr/bin/env python


import stocking.py as stocking
import rainbow.py as rainbow
import tree.py as tree
import unicornhathd
import signal


def shutdownHandler(sig, frame):
    print('Shutting down')
    unicornhathd.off()
    sys.exit(0)


signal.signal(signal.SIGINT, shutdownHandler)


THEO = 'Merry Christmas Theo!'
MARIA = 'Merry Christmas Maria!'
OWEN = 'Merry Christmas Owen!'

while True:
    stocking.drawStocking()
    rainbow.draw(THEO)
    tree.draw()
    rainbow.draw(MARIA)
    rainbow.draw(OWEN)
