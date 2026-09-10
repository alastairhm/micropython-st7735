# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-09-10

### Added
- `CLAUDE.md` with guidance for Claude Code sessions: deploy-to-board workflow,
  assumed Pico wiring, the buffer-less `TFT` driver architecture, per-tab init
  variants, and the `sysfont` layout.
- This changelog.

### Fixed
- `TFT.char()` glyph rendering (#3).

## [1.0.0] - 2024-11-30

### Added
- ST7735/ST7735S SPI TFT driver (`st7735` package) with red/blue/green tab init
  variants, primitive drawing (pixel, line, rect, circle, fill), text rendering,
  16-bit BMP blitting, and vertical scroll support.
- 5x8 bitmap font (`st7735.sysfont`).
- Examples: `hello_world.py`, `graphicstest.py`, `mandelbrot_tft.py`, `tftbmp.py`.

[Unreleased]: https://github.com/alastairhm/micropython-st7735/compare/1.1.0...HEAD
[1.1.0]: https://github.com/alastairhm/micropython-st7735/compare/1.0.0...1.1.0
[1.0.0]: https://github.com/alastairhm/micropython-st7735/releases/tag/1.0.0
