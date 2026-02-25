#include QMK_KEYBOARD_H

enum layers {
    BASE,
    BROWSER
};

enum custom_keycodes {
    LAYER_KEY = SAFE_RANGE
};

/* =========================
   FORWARD DECLARATION
   ========================= */
#ifdef OLED_ENABLE
void render_layer(void);
#endif

/* =========================
   KEYMAPS
   ========================= */

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

    [BASE] = LAYOUT(
        /* Top */
        LCTL(LSFT(KC_T)), LALT(KC_F4), LCTL(KC_F), LAYER_KEY,

        /* Middle */
        LCTL(KC_A), LCTL(KC_S), LGUI(LSFT(KC_S)), LCTL(KC_W),

        /* Bottom */
        LCTL(KC_C), LCTL(KC_V), LCTL(KC_Z), LALT(KC_TAB)
    ),

    [BROWSER] = LAYOUT(
        /* Top */
        LCTL(KC_D), LALT(KC_F4), LCTL(LSFT(KC_N)), LAYER_KEY,

        /* Middle */
        LCTL(KC_H), LCTL(KC_J), LCTL(KC_TAB), LCTL(LSFT(KC_TAB)),

        /* Bottom */
        LCTL(KC_T), LCTL(KC_F5), LCTL(KC_W), LALT(KC_TAB)
    )
};

/* =========================
   LAYER SWITCH (Stable)
   ========================= */

static uint8_t current_layer = BASE;

bool process_record_user(uint16_t keycode, keyrecord_t *record) {

    if (keycode == LAYER_KEY && record->event.pressed) {

        current_layer = (current_layer == BASE) ? BROWSER : BASE;

        layer_move(current_layer);

#ifdef OLED_ENABLE
        render_layer();
#endif

        return false;
    }

    return true;
}

/* =========================
   ENCODER
   ========================= */

bool encoder_update_user(uint8_t index, bool clockwise) {
    tap_code(clockwise ? KC_VOLU : KC_VOLD);
    return false;
}

/* =========================
   OLED
   ========================= */

#ifdef OLED_ENABLE

oled_rotation_t oled_init_user(oled_rotation_t rotation) {
    return OLED_ROTATION_180;
}

void render_base(void) {
    oled_clear();
    oled_write_ln_P(PSTR("REOPN CLS FIND LYR"), false);
    oled_write_ln_P(PSTR("ALL SAVE SHOT CLOSE"), false);
    oled_write_ln_P(PSTR("COPY PASTE UNDO ALT"), false);
}

void render_browser(void) {
    oled_clear();
    oled_write_ln_P(PSTR("BOOK CLS INCOG LYR"), false);
    oled_write_ln_P(PSTR("HIST DOWN NEXT PREV"), false);
    oled_write_ln_P(PSTR("NEWTAB REF CLOSE ALT"), false);
}

void render_layer(void) {

    if (current_layer == BASE) {
        render_base();
    } else {
        render_browser();
    }
}

void keyboard_post_init_user(void) {
    render_layer();
}

bool oled_task_user(void) {
    return false;   // No continuous redraw
}

#endif