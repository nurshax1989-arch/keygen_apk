"""AUTOCALL Keygen (Android). FAQAT DASTUR EGASI uchun - APK ni mijozlarga bermang!"""
import os
import time

from kivy.app import App
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from keycore import generate

BG, PANEL, FG, MUTED, ACC, OK, WARN = (0.043, 0.071, 0.125, 1), (0.07, 0.11, 0.19, 1), (0.92, 0.95, 1, 1), \
    (0.56, 0.65, 0.79, 1), (0.18, 0.66, 1, 1), (0.13, 0.77, 0.37, 1), (1, 0.69, 0.13, 1)


class KeygenApp(App):
    title = "AUTOCALL Keygen"
    icon = "icon.png"

    def build(self):
        Window.clearcolor = BG
        root = BoxLayout(orientation="vertical", padding=dp(20), spacing=dp(14))
        root.add_widget(Label(text="AUTOCALL Keygen", font_size=sp(26), bold=True, color=FG,
                              size_hint_y=None, height=dp(56)))
        root.add_widget(Label(text="Mijozning 8 xonali kompyuter kodini kiriting", color=MUTED,
                              font_size=sp(15), size_hint_y=None, height=dp(28)))
        self.inp = TextInput(multiline=False, input_filter="int", hint_text="1234 5678", halign="center",
                             font_size=sp(30), size_hint_y=None, height=dp(64), background_color=PANEL,
                             foreground_color=FG, cursor_color=ACC, padding=[dp(10), dp(14)])
        self.inp.bind(on_text_validate=lambda *_: self.go())
        root.add_widget(self.inp)
        root.add_widget(Button(text="Parol yaratish", font_size=sp(20), bold=True, background_normal="",
                               background_color=ACC, size_hint_y=None, height=dp(60), on_release=lambda *_: self.go()))
        self.out = Label(text="", font_size=sp(52), bold=True, color=OK, size_hint_y=None, height=dp(90))
        root.add_widget(self.out)
        self.note = Label(text="", color=WARN, font_size=sp(15), halign="center", valign="middle")
        self.note.bind(size=lambda w, s: setattr(w, "text_size", (s[0], None)))
        root.add_widget(self.note)
        root.add_widget(Label(text="Parol avtomatik nusxalanadi. Tarix: keygen_log.txt", color=MUTED,
                              font_size=sp(12), size_hint_y=None, height=dp(24)))
        return root

    def go(self):
        try:
            pw, note = generate(self.inp.text)
        except ValueError as exc:
            self.out.text, self.note.text = "", str(exc)
            return
        self.out.text, self.note.text = pw, note
        try:
            Clipboard.copy(pw)
        except Exception:  # noqa: BLE001
            pass
        try:
            with open(os.path.join(self.user_data_dir, "keygen_log.txt"), "a", encoding="utf-8") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}  kod={''.join(c for c in self.inp.text if c.isdigit())}  parol={pw}\n")
        except OSError:
            pass


if __name__ == "__main__":
    KeygenApp().run()
