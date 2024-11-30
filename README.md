# SPI TFT with ST7735 Driver library for Raspberry Pi Pico Micropython

## Acknowledgements

Based on work from

* [Guy Carver](https://github.com/GuyCarver)
* [boochow](https://github.com/boochow)


## Board used for examples

1.8" inch SPI LCD Screen Module 128*160 TFT with SD Card Slot ST7735 Driver

## Board Description

* 1.8-inch color screen, support 65K color display, display rich colors
* 128X160 resolution, clear display
* Using the SPI serial bus, it only takes a few IOs to light up the display


### Product parameters

* Display color: 16BIT RGB 65K color
* Screen Size: 1.8 (inches)
* Type: TFT
* Driver IC: ST7735S
* Resolution: 128*160 (pixels)
* Module interface: 4-wire SPI interface
* Backlight: 2 white LEDs
* Effective area: 28.03x35.04 (mm)
* Module PCB Dimensions: 38.30x62.48 (mm)
* Working temperature: -20℃~60℃
* Storage temperature: -30℃~70℃
* Working voltage: 5V/3.3V
* Weight: 16g

## Wiring TFT display to the Raspberry Pi Pico

This is the pin wiring used in the examples code.

| TFT Board | Raspberry Pi Pin |
|:--------:|:-------------:|
| LED | 3v3(Out)|
| SCK | GP10 |
| SDA | GP11 |
| AO/DC | GP16 |
| Reset | GP17 |
| CS | GP18 |
| GND | GND |
| VCC | VBUS 5V |

## Installation 

Upload the directory [st7735](st7735) to your Raspberry Pi Pico.

Upload the BMP files to the root directory to be accessed by [tftbmp.py](tftbmp.py), 

*NOTE* The BMP files will need to be in 24bit format. Thank to [Stu McGee](https://github.com/StuMunsonMcGee) for that information as I had forgotten to include it.

## Example in my blog

* https://blog.0x32.co.uk/posts/pico8/

