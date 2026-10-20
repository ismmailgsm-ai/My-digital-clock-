
__version__ = "1.0.0"

from datetime import datetime
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex


class DigitalClockApp(App):

    def build(self):
        self.title = "My Digital Clock"

        Window.clearcolor = get_color_from_hex("#101820")

        layout = BoxLayout(
            orientation="vertical",
            padding=[24, 40, 24, 30],
            spacing=18
        )

        layout.add_widget(Widget())

        title = Label(
            text="MY DIGITAL CLOCK",
            font_size="20sp",
            bold=True,
            color=get_color_from_hex("#65E8C0"),
            size_hint_y=None,
            height=50
        )
        layout.add_widget(title)

        self.time_label = Label(
            text="00:00:00",
            font_size="54sp",
            bold=True,
            color=get_color_from_hex("#65E8C0"),
            size_hint_y=None,
            height=100
        )
        layout.add_widget(self.time_label)

        self.date_label = Label(
            text="",
            font_size="20sp",
            color=get_color_from_hex("#FFFFFF"),
            size_hint_y=None,
            height=45
        )
        layout.add_widget(self.date_label)

        self.day_label = Label(
            text="",
            font_size="17sp",
            color=get_color_from_hex("#B6C6CF"),
            size_hint_y=None,
            height=40
        )
        layout.add_widget(self.day_label)

        layout.add_widget(Widget())

        footer = Label(
            text="TIME • DATE • SIMPLE",
            font_size="13sp",
            color=get_color_from_hex("#65E8C0"),
            size_hint_y=None,
            height=35
        )
        layout.add_widget(footer)

        layout.add_widget(Widget())

        self.update_clock(0)
        Clock.schedule_interval(self.update_clock, 1)

        return layout

    def update_clock(self, dt):
        now = datetime.now()

        self.time_label.text = now.strftime("%H:%M:%S")
        self.date_label.text = now.strftime("%d/%m/%Y")
        self.day_label.text = now.strftime("%A")


if __name__ == "__main__":
    DigitalClockApp().run()
