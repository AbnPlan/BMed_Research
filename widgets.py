
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import ButtonBehavior
from kivy.uix.image import Image
from screens import *

class PicButton(ButtonBehavior, Image):
    '''Class that makes it possible to have an Image that works like a Button'''
    pass

class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.add_widget(MenuScreen(name='menu'))
        self.add_widget(EntryForm(name='entry'))
        self.add_widget(Appointments(name='appointments'))
        self.add_widget(Survey(name='survey'))
        self.add_widget(Info(name='info'))

    def SMMainScreen(self):
        '''Change screen to Main Menu'''
        self.current = 'menu'

    def SMEntry(self):
        '''Change screen to Entry'''
        self.current = 'entry'

    def SMAppointments(self):
        '''Change screen to Appointments'''
        self.current = 'appointments'

    def SMsurvey(self):
        '''Change screen to Survey'''
        self.current = 'survey'

    def SMInfo(self):
        '''Change screen to Info'''
        self.current = 'info'
