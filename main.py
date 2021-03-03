import kivy
kivy.require('2.0.0')

from screens import *

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, RiseInTransition
from kivy.uix.checkbox import CheckBox
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

Builder.load_file('main.kv')
Window.size = (1024, 600)
Window.borderless = True

class MainApp(App):
    '''Contains the main app and the tittle of the app'''
    def build(self):
        '''Builds the app by returning the Screen Manager'''
        return MyScreenManager(transition=RiseInTransition())

if __name__ == "__main__":
    MainApp().run()
