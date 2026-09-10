# TODO

Known issues found in `st7735/__init__.py` and the examples. Ordered roughly by
severity. None break the paths the current examples exercise on the reference
128x160 red-tab panel.

## Bugs

- [ ] **`circle()` crashes past the left/top edge** (`st7735/__init__.py:322`).
  No bounds check, unlike `pixel()`. When `xn`/`yn` goes negative it reaches
  `_setwindowpoint()`, which assigns a negative value into the `windowLocData`
  bytearray -> `ValueError: bytes value out of range`. Any circle outline
  crossing x=0 or y=0 (or going beyond 255) throws;
  `graphicstest.testdrawcircles(10, ...)` hits it. `fillcircle()` is safe (routes
  through the clamping `vline()`). Fix: guard each octant point like `pixel()`
  does.

- [ ] **`_draw()` gets the raw length, not the clamped span**
  (`st7735/__init__.py:268`, `:280`, `:408`). `vline`/`hline` compute a clamped
  start/stop then call `self._draw(aLen)` with the original argument.
  - Negative length (documented as allowed) yields a garbage count:
    `_draw(-5)` writes `-5 % 32 == 27` pixels.
  - A line clipped at the screen edge still streams the full `aLen`; the ST7735
    wraps inside the address window, so it is harmless overdraw but not intended.

- [ ] **Off-by-one in edge clamping** (`st7735/__init__.py:270`, `:283`, `:304`,
  `:364`). `vline`/`hline`/`fillrect`/`fillcircle` clamp to `self._size[N]`; the
  last valid pixel is `self._size[N] - 1`, so the address window can be set one
  column/row past the panel.

- [ ] **`line()` never plots the final endpoint** (`st7735/__init__.py:248`,
  `:259`). The Bresenham loops are `while px != ex` / `while py != ey`, so
  diagonal lines stop one pixel short of `aEnd`. Horizontal/vertical lines are
  fine (they use `abs(diff) + 1`).

- [ ] **`initb()` inflates `_size` but never sets `_offset`**
  (`st7735/__init__.py:504`). Does `self._size = (w + 2, h + 1)` with no matching
  `_offset`, unlike `initb2()` (`_offset = [2, 1]`). Blue-tab output is shifted
  with a couple of unaddressable columns/row.

- [ ] **`rotation()` swaps `_size` but not `_offset`**
  (`st7735/__init__.py:144`). For panels needing a non-zero offset, rotating
  leaves the offset on the wrong axis.

## Minor / cosmetic

- [ ] Stale `__init__` docstring (`st7735/__init__.py:108`) - describes an `aLoc`
  "1 for 'X' or 2 for 'Y'" argument that no longer exists; signature is
  `(spi, aDC, aReset, aCS, ScreenSize)`.
- [ ] `setvscroll`/`vscroll` hardcode `162` (`st7735/__init__.py:383`, `:392`),
  assuming the 160-px reference panel.
- [ ] Mislabeled color constants (`st7735/__init__.py:93`, `:98`): `FOREST` is
  teal `(0, 0x80, 0x80)`, `PURPLE` is magenta `(0xFF, 0, 0xFF)`.
- [ ] `mandelbrot_tft.py` sets `width=160`/`height=128` then calls
  `tft.pixel([y, x], ...)` with the axes swapped - lands in bounds but reads
  backwards.
- [ ] Module-level `maker`/`makeb`/`makeg` helpers
  (`st7735/__init__.py:893`-`912`) use the old `TFT(1, "X1", "X2")` signature and
  would fail if called.
