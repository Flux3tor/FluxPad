# FluxPad

FluxPad is a custom-built 12-key macropad designed for productivity, development workflows, and media control. It is built around the Seeed XIAO RP2040 and features per-key RGB lighting, a rotary encoder, and an OLED status display.

This project was created as part of Hack Club’s Blueprint program and includes a custom PCB, firmware, and a 3D-printed case.

---

## Features

- 12 MX-style mechanical keys (4×3 layout)
- Seeed XIAO RP2040 microcontroller
- Rotary encoder (volume)
- 0.91" OLED display (I²C)
- KMK firmware (CircuitPython)
- Custom 3D-printed case with heatset inserts

---

## Hardware Overview

### Microcontroller
- **Seeed XIAO RP2040**
- USB-C interface
- RP2040 dual-core MCU

### Input Devices
- 12 × MX-style switches
- 1 × EC11 rotary encoder

### Output Devices
- 1 × 0.91" OLED display (I²C)

### Power
- Powered via USB through the XIAO RP2040

---

## Firmware

FluxPad uses **KMK**, a Python-based keyboard firmware built on CircuitPython.

### Why KMK?
- Faster iteration (no compiling)
- Clean support for RP2040
- Simple handling of direct-wired keys
- Easy RGB, encoder, and OLED integration

The main firmware logic lives in `main.py`.

---

## Key Layout

FluxPad uses a 3-layer setup:

### Layer 0 – Base
- Copy, Paste, Undo, Redo
- Screenshot, Task View, Lock, File Explorer
- Layer switching and utility keys

### Layer 1 – Dev
- Editor shortcuts
- Terminal, browser, build/run
- Escape and tab access

### Layer 2 – Media
- Play/Pause, Next, Previous
- Brightness control

The rotary encoder controls system volume.

---

## OLED Display

The OLED displays:
- Device name
- Active layer
- Encoder mode
- Optional key feedback

The display is intentionally kept minimal for clarity and performance.

---
