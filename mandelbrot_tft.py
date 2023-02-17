#!/usr/bin/env python
# -*- coding: utf-8 -*-

# From http://warp.povusers.org/MandScripts/python.html

from machine import SPI, Pin
from st7735 import TFT, TFTColor

spi = SPI(
    1, baudrate=20000000, polarity=0, phase=0, sck=Pin(10), mosi=Pin(11), miso=None
)
tft = TFT(spi, 16, 17, 18)
tft.initr()
tft.rgb(True)
tft.fill(TFT.BLACK)

minX = -2.0
maxX = 1.0
width = 160
height = 128
aspectRatio = 1.25

chars = " .,-:;i+hHM$*#@ "
clen = len(chars)
colours = [
    TFTColor(0xF0, 0x20, 0x20),
    TFT.RED,
    TFT.MAROON,
    TFT.GREEN,
    TFT.FOREST,
    TFT.BLUE,
    TFT.NAVY,
    TFT.CYAN,
    TFT.YELLOW,
    TFT.PURPLE,
    TFT.WHITE,
    TFT.GRAY,
    TFT.RED,
    TFT.MAROON,
    TFT.GREEN,
    TFT.FOREST,
    TFT.BLACK,
]

rangeX = maxX - minX
yScale = (rangeX) * (float(height) / width) * aspectRatio

for y in range(height):
    line = ""
    ytemp = y * yScale / height - yScale / 2
    for x in range(width):
        c = complex(minX + x * (rangeX) / width, ytemp)
        z = c
        colour = 0
        while abs(z) <= 2 and colour < clen:
            colour += 1
            z = z * z + c
        tft.pixel([y, x], colours[colour])
        line += chars[colour % clen]
    print(line)
