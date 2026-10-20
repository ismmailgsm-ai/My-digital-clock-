
__version__ = "2.0.0"

from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget


BACKGROUND = "#080B12"
CYAN = "#65E8C0"
WHITE = "#FFFFFF"
MUTED = "#9AA8B7"

DAYS = [
    "الاثنين",
    "الثلاثاء",
    "الأربعاء",
    "الخميس",
    "الجمعة",
    "السبت",
    "الأحد",
]

MONTHS = [
    "يناير", "فبراير", "مارس", "أبريل",
    "مايو", "يونيو", "يوليو", "أغسطس",
    "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"
]


class DigitalClockApp(App):

    def build(self):
        self.title = "My Digital Clock"
        Window.clearcolor = get_color_from_hex(BACKGROUND)

        layout = BoxLayout(
            orientation="vertical",
            padding=[20, 30, 20, 25],
            spacing=12
        )

        layout.add_widget(Widget())

        self.heading = Label(
            text="MY DIGITAL CLOCK",
            font_size="20sp",
            bold=True,
            color=get_color_from_hex(CYAN),
            size_hint_y=None,
            height=55
        )
        layout.add_widget(self.heading)

        self.time_label = Label(
            text="00:00:00",
            font_size="54sp",
            bold=True,
            color=get_color_from_hex(CYAN),
            size_hint_y=None,
            height=110,
            halign="center",
            valign="middle"
        )
        layout.add_widget(self.time_label)

        self.date_label = Label(
            text="",
            font_size="21sp",
            color=get_color_from_hex(WHITE),
            size_hint_y=None,
            height=55
        )
        layout.add_widget(self.date_label)

        self.day_label = Label(
            text="",
            font_size="20sp",
            color=get_color_from_hex(MUTED),
            size_hint_y=None,
            height=45
        )
        layout.add_widget(self.day_label)

        layout.add_widget(Widget())

        self.footer = Label(
            text="TIME  •  DATE  •  SIMPLE",
            font_size="13sp",
            color=get_color_from_hex(CYAN),
            size_hint_y=None,
            height=40
        )
        layout.add_widget(self.footer)

        layout.add_widget(Widget())

        self.update_clock(0)
        Clock.schedule_interval(self.update_clock, 1)

        return layout

    def update_clock(self, dt):
        now = datetime.now()

        self.time_label.text = now.strftime("%H:%M:%S")

        self.date_label.text = (
            f"{now.day} {MONTHS[now.month - 1]} {now.year}"
        )

        self.day_label.text = DAYS[now.weekday()]


if __name__ == "__main__":
    DigitalClockApp().run()
