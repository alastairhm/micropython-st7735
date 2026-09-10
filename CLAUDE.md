# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A pure-MicroPython driver for SPI TFT displays using the ST7735/ST7735S controller
(1.8" 128x160 being the reference panel), targeted at the Raspberry Pi Pico. There
is no build, no package manager, and no test suite — the code only runs on a
microcontroller with a physical display attached. "Running" it means copying files
to the board and executing an example.

## Deploying to a board

Copy the `st7735/` package to the board's filesystem (root or `/lib`), plus any
example you want to run and its BMP assets. Typical tools:

```sh
mpremote connect /dev/ttyACM0 fs cp -r st7735 :        # upload the package
mpremote connect /dev/ttyACM0 fs cp tux.bmp :          # upload an asset
mpremote connect /dev/ttyACM0 run graphicstest.py      # run an example without copying it
```

`rshell` or Thonny work equally well. BMP files consumed by `tftbmp.py` must be
**24-bit uncompressed**.

## Wiring assumed by every example

SPI1 on the Pico: SCK=GP10, MOSI(SDA)=GP11, DC(AO)=GP16, RESET=GP17, CS=GP18,
20 MHz baudrate, `miso=None`. Change the `SPI(...)` and `TFT(spi, 16, 17, 18)`
lines if the hardware differs.

## Architecture

- **`st7735/__init__.py`** — the entire driver, one `TFT` class. No `framebuf`,
  no off-screen buffer: every drawing call translates directly into ST7735
  command/data sequences pushed over SPI. Key internals:
  - `_writecommand` / `_writedata` toggle the DC and CS pins around
    `spi.write(...)`. All higher-level methods are built on these.
  - `_setwindowpoint` / `_setwindowloc` program the CASET/RASET address window,
    then `_setColor` + `_draw` stream a repeated 2-byte color (chunked 32 pixels
    at a time via a preallocated `self.buf`) to fill it. This is why `fill`,
    `fillrect`, `hline`, `vline` are fast and `pixel`/`circle` (per-point) are slow.
  - `_offset` and `_size` handle the per-panel dead pixels and rotation. `_size`
    is swapped on 90/270 rotation; `rotation()` and `rgb()` both re-issue MADCTL
    via `_setMADCTL`.
  - Colors are RGB565 16-bit ints. `TFTColor(r,g,b)` (module function) or
    `TFT.color(r,g,b)` build them; named constants (`TFT.RED`, etc.) live on the class.
  - **Panel init variants**: `initr()` (red tab), `initb()` / `initb2()` (blue tab),
    `initg()` (green tab). These differ in gamma/power register values and pixel
    offsets — pick the one matching the physical display's tab color. Examples use
    `initr()`. The `maker`/`makeb`/`makeg` helper functions at the bottom of the
    file are legacy (stale `TFT(1, "X1", "X2")` signature) and unused.
  - `text()` calls `char()` per glyph; `char()` renders each font column as
    `fillrect` calls, so scaling (`aSize`) is free.
- **`st7735/sysfont.py`** — one dict `sysfont` = a 5x8 bitmap font, one byte per
  column, indexed by `(ord(c) - Start) * Width` into `Data`. Passed as the `aFont`
  argument to `text()`/`char()`. Any dict with `Width/Height/Start/End/Data` keys
  in the same layout works as a font.

## Examples (run as `__main__`)

- `hello_world.py` — minimal scaled-text demo.
- `graphicstest.py` — exercises lines, rects, circles, triangles, text (Adafruit
  graphicstest port).
- `mandelbrot_tft.py` — per-pixel plot; also prints ASCII to the REPL.
- `tftbmp.py` — parses a 24-bit BMP by hand and streams it via `_pushcolor`.

## Conventions

The driver code uses 2-space indent, `aName` argument prefixes, and `_name`
private methods — a Guy Carver / boochow inheritance. The example scripts use
plain 4-space PEP 8. Match whichever file you are editing. Commented-out
`@micropython.native` decorators are deliberate — left as opt-in speedups.

Record user-facing changes in `CHANGELOG.md` (Keep a Changelog format) under
`## [Unreleased]`.
