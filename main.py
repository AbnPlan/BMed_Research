import kivy
kivy.require('2.0.0')

from screens import MenuScreen
from screens import EntryForm
from screens import Appointments
from screens import Survey
from screens import Info

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput

class MainApp(App):
    '''Contains the main app and the tittle of the app'''
    title = 'Med'
    def build(self):
        '''Builds the app by returning the MainWidget from Kivi file'''
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(EntryForm(name='entry'))
        sm.add_widget(Appointments(name='appointments'))
        sm.add_widget(Survey(name='survey'))
        sm.add_widget(Info(name='info'))

        return sm

class MainButtons(ButtonBehavior, Image):
    '''Class that makes it possible to have an Image that works like a Button'''
    def test_button(self, i): 
        '''Button test function'''
        print(f"Pressed Button {i}") 


if __name__ == "__main__":
    Builder.load_file('main.kv')
    Window.size = (1024, 600)
    Window.borderless = True
    MainApp().run()
