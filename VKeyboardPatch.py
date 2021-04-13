# Source: https://stackoverflow.com/questions/35951863/kivy-virtual-keyboard-how-to-handle-modifier-keys-e-g-shift-without-multi
from kivy.uix.vkeyboard import VKeyboard


def process_key_on(self, touch):
    if not touch:
        return
    x, y = self.to_local(*touch.pos)
    key = self.get_key_at_pos(x, y)
    if not key:
        return

    key_data = key[0]
    displayed_char, internal, special_char, size = key_data
    line_nb, key_index = key[1]

    # save pressed key on the touch
    ud = touch.ud[self.uid] = {}
    ud['key'] = key

    # for caps lock or shift only:
    uid = touch.uid
    if special_char is not None:
        # Do not repeat special keys
        if special_char in ('capslock', 'shift', 'layout', 'special'):
            if self._start_repeat_key_ev is not None:
                self._start_repeat_key_ev.cancel()
                self._start_repeat_key_ev = None
            self.repeat_touch = None
        if special_char == 'capslock':
            self.have_shift = False
            self.have_capslock = not self.have_capslock
            uid = -1
        elif special_char == 'shift':
            self.have_capslock = False
            self.have_shift = not self.have_shift
            uid = -1
        elif special_char == 'special':
            self.have_special = True
        elif special_char == 'layout':
            self.change_layout()

    # send info to the bus
    b_keycode = special_char
    b_modifiers = self._get_modifiers()
    if self.get_parent_window().__class__.__module__ == \
            'kivy.core.window.window_sdl2' and internal:
        self.dispatch('on_textinput', internal)
    else:
        self.dispatch('on_key_down', b_keycode, internal, b_modifiers)

    if special_char is not None and \
            special_char != 'shift' and \
            self.have_shift:
        self.have_shift = False
        self.active_keys = []
    else:
        # save key as an active key for drawing
        self.active_keys[uid] = key[1]

    self.refresh_active_keys_layer()


def process_key_up(self, touch):
    uid = touch.uid
    if self.uid not in touch.ud:
        return

    # save pressed key on the touch
    key_data, key = touch.ud[self.uid]['key']
    displayed_char, internal, special_char, size = key_data

    # send info to the bus
    b_keycode = special_char
    b_modifiers = self._get_modifiers()
    self.dispatch('on_key_up', b_keycode, internal, b_modifiers)

    if special_char in ('shift', 'capslock'):
        uid = -1

    if uid in self.active_keys:
        self.active_keys.pop(uid, None)
        if special_char == 'shift' and self.have_shift:
            self.active_keys[-1] = key
        elif special_char == 'special':
            self.have_special = False
        if special_char == 'capslock' and self.have_capslock:
            self.active_keys[-1] = key
        self.refresh_active_keys_layer()


VKeyboard.process_key_on = process_key_on
VKeyboard.process_key_up = process_key_up
