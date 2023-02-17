'''
Testing graphics on TFT display with ST7735 controller connected to Raspberry Pi Pico
'''

from st7735 import TFT
from st7735 import sysfont
from machine import SPI,Pin
import time
import math

def tftprinttest(font):
    tft.fill(TFT.BLACK);
    v = 30
    tft.text((0, v), "Hello World!", TFT.RED, font, 1, nowrap=True)
    v += font["Height"]
    tft.text((0, v), "Hello World!", TFT.YELLOW, font, 2, nowrap=True)
    v += font["Height"] * 2
    tft.text((0, v), "Hello World!", TFT.GREEN, font, 3, nowrap=True)
    v += font["Height"] * 3
    tft.text((0, v), str(1234.567), TFT.BLUE, font, 4, nowrap=True)
    time.sleep_ms(1500)

def test_main():
    tftprinttest(sysfont.sysfont)
    time.sleep_ms(100)

if __name__ == "__main__":
    spi = SPI(1, baudrate=20000000, polarity=0, phase=0,
              sck=Pin(10), mosi=Pin(11), miso=None)
    tft=TFT(spi,16,17,18)
    tft.initr()
    tft.rgb(True)
    test_main()
