
import kivy
kivy.require('2.0.0')

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'dock')

from widgets import *
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
import VKeyboardPatch
from kivy.uix.screenmanager import RiseInTransition

Builder.load_file('main.kv')
Builder.load_file('./KV_SCREENS/appointments.kv')
Builder.load_file('./KV_SCREENS/entry_form.kv')
Builder.load_file('./KV_SCREENS/info.kv')
Builder.load_file('./KV_SCREENS/menu_screen.kv')
Builder.load_file('./KV_SCREENS/survey.kv')

Window.size = (1024, 600)
Window.borderless = True

class MainApp(MDApp):
    '''Contains the main app and the title of the app'''
    def build(self):
        '''Builds the app by returning the Screen Manager'''
        self.theme_cls.primary_palette = "LightBlue"
        return MyScreenManager(transition = RiseInTransition())


if __name__ == "__main__":
    MainApp().run()
