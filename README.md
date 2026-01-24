# FluxPad

FluxPad is a custom 12-key macropad powered by the Seeed XIAO RP2040.  
It features a rotary encoder for volume and scrolling, an OLED status display, and a compact 3D-printed case designed for daily productivity and creative workflows.

---

## Features
- 12 MX mechanical keys
- Rotary encoder (volume + scroll control)
- 0.91" OLED display (layer & status display)
- Seeed XIAO RP2040 microcontroller
- KMK firmware (CircuitPython-based)
- Fully custom 2-layer PCB
- 3D-printed case

---

## Project Images

### Schematic
![Schematic](Images/schematic.png)

### PCB
![PCB](Images/pcb.png)

### Case Design
#### Bottom Case
![case_bottom](Images/case_bottom.png)

#### Top Case
![case_top](Images/case_top.png)

### Final Layout
![Final](Images/case_assembled.png)

---

## System Overview

### MCU
- Seeed Studio XIAO RP2040 (Through-hole)

### Inputs
- 12x MX mechanical switches
- 1x EC11 rotary encoder

### Output
- 0.91" OLED display (I2C)

---

## Pin Mapping

| Function | GPIO |
|----------|------|
| ROW0 | GPIO26 |
| ROW1 | GPIO27 |
| ROW2 | GPIO28 |
| COL0 | GPIO29 |
| COL1 | GPIO0 |
| COL2 | GPIO1 |
| COL3 | GPIO2 |
| Encoder A | GPIO4 |
| Encoder B | GPIO3 |
| OLED SDA | GPIO6 |
| OLED SCL | GPIO7 |

---

## Bill of Materials (BOM)

| Part | Quantity | Manufacturer | Part Number |
|------|----------|--------------|-------------|
| Seeed XIAO RP2040 (TH) | 1 | Seeed Studio | 102010428 |
| MX Mechanical Switch | 12 | Gateron / Kailh | MX-Style |
| 1N4148 Diodes (TH) | 12 | Vishay | 1N4148 |
| SK6812 MINI-E RGB LED | 0 | — | — |
| EC11 Rotary Encoder | 1 | ALPS / Generic | EC11 |
| 0.91" OLED Display | 1 | Generic | SSD1306 |
| DSA Keycaps | 12 | Generic | DSA Blank |
| M3x16 Screws | 4 | Generic | M3 |
| Heatset Inserts | 4 | Generic | M3 |

---

## Firmware
FluxPad runs on KMK (CircuitPython-based firmware).  
The firmware supports:
- Key matrix scanning
- Encoder volume & scroll control
- OLED display support

Source code is located in the `Firmware/` folder.

---

## Case
The case is fully 3D printed and designed in Fusion360.  
It consists of:
- Bottom shell
- Top plate
- Heatset insert mounts

Exported as a single STEP file in the `CAD/` folder.

---

## Future Upgrades
- RGB underglow support
- Multiple firmware layers
- Macro recording mode
- Animated OLED UI

---

## Author
Designed and built by **Flux3tor**  
Hack Club Hackpad Project
