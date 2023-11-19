from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from instructions import *


class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction, color=(1, .66, .34, 1), bold=True)
        lbl_name = Label(text="Введіть імʼя:", halign='right', color=(1, .66, .34, 1), bold=True, font_size=40)
        self.input_name = TextInput(text="Микола", multiline=False)
        lbl_age = Label(text="Введіть вік:", halign='right', color=(1, .66, .34, 1), bold=True, font_size=40)
        self.input_age = TextInput(text="7", multiline=False)
        self.btn = Button(text='Почати', size_hint=(.3, .2), pos_hint={'center_x': .5}, bold=True, background_color=(.29, .53, .94, 1))
        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(.8, None), height="30sp")
        line2 = BoxLayout(size_hint=(.8, None), height="30sp")

        line1.add_widget(lbl_name)
        line1.add_widget(self.input_name)

        line2.add_widget(lbl_age)
        line2.add_widget(self.input_age)

        main_line = BoxLayout(orientation='vertical', padding=10, spacing=15)
        main_line.add_widget(instr)
        main_line.add_widget(line1)
        main_line.add_widget(line2)
        main_line.add_widget(self.btn)

        self.add_widget(main_line)

    def next(self):
        self.manager.current = 'second'

class PulseScr(Screen):
    pass

class SitsScr(Screen):
    pass

class PulseScr2(Screen):
    pass

class ResultScr(Screen):
    pass


class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='first'))
        sm.add_widget(PulseScr(name='second'))
        sm.add_widget(SitsScr(name='third'))
        sm.add_widget(PulseScr2(name='fourth'))
        sm.add_widget(ResultScr(name='fifth'))
        return sm


app = HeartCheck()
app.run()



