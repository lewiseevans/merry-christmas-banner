#!/usr/bin/env python


import stocking
import rainbow
import tree
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
    rainbow.draw(THEO)
    tree.draw()
    rainbow.draw(MARIA)
    stocking.draw()
    rainbow.draw(OWEN)
