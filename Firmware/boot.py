# ==============================
# FLUXPAD FIRMWARE
# Built by Flux3tor
# 12 Keys + OLED + Encoder
# ==============================

import board
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.oled import OLED
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap

# ==============================
# KEYBOARD CORE
# ==============================
keyboard = KMKKeyboard()

# ==============================
# MATRIX CONFIG
# ==============================
keyboard.row_pins = (board.GP26, board.GP27, board.GP28)
keyboard.col_pins = (board.GP29, board.GP0, board.GP1, board.GP2)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ==============================
# MODULES
# ==============================
layers = Layers()
encoder = EncoderHandler()
macros = Macros()

keyboard.modules.append(layers)
keyboard.modules.append(encoder)
keyboard.modules.append(macros)

# ==============================
# ENCODER
# ==============================
# A → GPIO4
# B → GPIO3
encoder.pins = (
    (board.GP4, board.GP3),
)

encoder.map = [
    ((KC.VOLD, KC.VOLU),),  # Layer 0
    ((KC.LEFT, KC.RIGHT),) # Layer 1 (Scroll / timeline control)
]

# ==============================
# OLED
# ==============================
oled = OLED(
    sda=board.GP6,
    scl=board.GP7,
    i2c_addr=0x3C,
    width=128,
    height=32
)

keyboard.extensions.append(oled)

# ==============================
# MACROS
# ==============================
OPEN_BROWSER = KC.Macro(
    Press(KC.LGUI),
    Tap(KC.B),
    Release(KC.LGUI)
)

OPEN_EXPLORER = KC.Macro(
    Press(KC.LGUI),
    Tap(KC.E),
    Release(KC.LGUI)
)

LOCK_PC = KC.Macro(
    Press(KC.LGUI),
    Tap(KC.L),
    Release(KC.LGUI)
)

TASK_VIEW = KC.Macro(
    Press(KC.LGUI),
    Tap(KC.TAB),
    Release(KC.LGUI)
)

OPEN_VSCODE = KC.Macro(
    Press(KC.LGUI),
    Tap(KC.R),
    Release(KC.LGUI),
    Tap(KC.C),
    Tap(KC.O),
    Tap(KC.D),
    Tap(KC.E),
    Tap(KC.ENTER)
)

OPEN_TERMINAL = KC.Macro(
    Press(KC.LGUI),
    Tap(KC.R),
    Release(KC.LGUI),
    Tap(KC.C),
    Tap(KC.M),
    Tap(KC.D),
    Tap(KC.ENTER)
)

WIN_SEARCH = KC.Macro(
    Press(KC.LGUI),
    Tap(KC.S),
    Release(KC.LGUI)
)

RUN_DIALOG = KC.Macro(
    Press(KC.LGUI),
    Tap(KC.R),
    Release(KC.LGUI)
)

TASK_MANAGER = KC.Macro(
    Press(KC.LCTRL),
    Press(KC.LSHIFT),
    Tap(KC.ESC),
    Release(KC.LSHIFT),
    Release(KC.LCTRL)
)

# ==============================
# KEYMAP
# ==============================
keyboard.keymap = [

    # ===== LAYER 0 — MEDIA MODE =====
    [
        KC.MPLY, KC.MPRV, KC.MNXT, KC.MUTE,
        KC.VOLD, KC.VOLU, TASK_VIEW, LOCK_PC,
        OPEN_BROWSER, OPEN_EXPLORER, KC.TG(1), KC.LGUI
    ],

    # ===== LAYER 1 — DEV MODE =====
    [
        KC.ESC, KC.COPY, KC.PASTE, TASK_MANAGER,
        KC.ALT_TAB, KC.CTRL_S, OPEN_VSCODE, OPEN_TERMINAL,
        WIN_SEARCH, RUN_DIALOG, KC.TG(0), KC.ENTER
    ]
]

# ==============================
# OLED DISPLAY TASK
# ==============================
def oled_task():
    oled.clear()
    oled.text("FLUXPAD", 0, 0, 1)

    if keyboard.active_layers[0] == 0:
        oled.text("MODE: MEDIA", 0, 12, 1)
    else:
        oled.text("MODE: DEV", 0, 12, 1)

    oled.text("STATUS: ONLINE", 0, 24, 1)
    oled.show()

keyboard.oled_task = oled_task

# ==============================
# START
# ==============================
if __name__ == "__main__":
    print("FluxPad booting...")
    time.sleep(1)
    keyboard.go()
