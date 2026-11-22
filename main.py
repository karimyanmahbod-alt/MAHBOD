
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.metrics import dp
import arabic_reshaper
from bidi.algorithm import get_display


def fa(text):
    return get_display(arabic_reshaper.reshape(str(text)))


class MahbodApp(App):

    title = "مهبد"

    def build(self):
        Window.clearcolor = (0.06, 0.08, 0.15, 1)

        root = BoxLayout(
            orientation="vertical",
            padding=dp(25),
            spacing=dp(18)
        )

        root.add_widget(Label(
            text=fa("مهبد"),
            font_size="34sp",
            color=(0.5, 0.4, 1, 1),
            bold=True
        ))

        root.add_widget(Label(
            text=fa("برنامه محاسبه سن شما"),
            font_size="17sp",
            color=(0.7, 0.75, 0.85, 1)
        ))

        self.name_input = TextInput(
            hint_text=fa("اسم خود را وارد کنید"),
            multiline=False,
            halign="center",
            font_size="18sp",
            size_hint_y=None,
            height=dp(55)
        )
        root.add_widget(self.name_input)

        self.age_input = TextInput(
            hint_text=fa("چند سالته؟"),
            multiline=False,
            input_filter="int",
            halign="center",
            font_size="18sp",
            size_hint_y=None,
            height=dp(55)
        )
        root.add_widget(self.age_input)

        calculate = Button(
            text=fa("محاسبه سن"),
            font_size="19sp",
            size_hint_y=None,
            height=dp(58),
            background_normal="",
            background_color=(0.45, 0.32, 1, 1)
        )
        calculate.bind(on_press=self.calculate)
        root.add_widget(calculate)

        clear = Button(
            text=fa("پاک کردن اطلاعات"),
            font_size="16sp",
            size_hint_y=None,
            height=dp(50),
            background_normal="",
            background_color=(0.17, 0.22, 0.33, 1)
        )
        clear.bind(on_press=self.clear)
        root.add_widget(clear)

        self.result = Label(
            text="",
            font_size="17sp",
            color=(0.25, 0.9, 0.65, 1)
        )
        root.add_widget(self.result)

        return root

    def calculate(self, instance):
        name = self.name_input.text.strip()
        age_text = self.age_input.text.strip()

        if not name or not age_text:
            self.result.text = fa("لطفاً همه اطلاعات را وارد کن")
            return

        age = int(age_text)

        if age < 0 or age > 120:
            self.result.text = fa("سن وارد شده معتبر نیست")
            return

        if age < 18:
            message = (
                f"سلام {name} عزیز!\n"
                f"سن تو {age} ساله است.\n"
                f"{18-age} سال تا ۱۸ سالگی باقی مانده!"
            )
        elif age == 18:
            message = f"سلام {name}!\nتو دقیقاً ۱۸ سالته!"
        else:
            message = (
                f"سلام {name}!\n"
                f"تو {age} سالته.\n"
                f"{age-18} سال از ۱۸ سالگیت گذشته!"
            )

        self.result.text = fa(message)

    def clear(self, instance):
        self.name_input.text = ""
        self.age_input.text = ""
        self.result.text = ""


MahbodApp().run()
