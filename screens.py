import db_manager as db

from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import ButtonBehavior
from kivy.uix.image import Image

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


class PicButton(ButtonBehavior, Image):
    '''Class that makes it possible to have an Image that works like a Button'''
    pass

class MenuScreen(Screen):
    '''Main menu screen'''
    pass

class EntryForm(Screen):
    '''Entry form screen'''
    def clear_text(self):
        '''Clear all textboxes'''
        self.ids.full_name.text = ''
        self.ids.phone_number.text = ''
        self.ids.address_line1.text = ''
        self.ids.address_line2.text = ''
        self.ids.town.text = ''
        self.ids.country.text = 'Puerto Rico'
        self.ids.zip_code.text = ''
        self.ids.health_insurance.text = ''

    def save_form(self):
        '''Save form into Database'''
        db_connection = db.db_connection()
        db.insert_data(
            db_connection, 
            self.ids.full_name.text,
            self.ids.phone_number.text,
            self.ids.address_line1.text,
            self.ids.address_line2.text,
            self.ids.town.text,
            self.ids.country.text,
            self.ids.zip_code.text,
            self.ids.health_insurance.text
        )

        db_connection.close()


class Appointments(Screen):
    '''APPOINTMENTS SCREEN'''
    pass

class Survey(Screen):
    '''Survey screen'''
    pass

class Info(Screen):
    '''Info screen'''
    def build(self):
        self.ids.layout.remove_widget(self.ids.slide_1)
        self.ids.layout.remove_widget(self.ids.slide_2)
        self.ids.layout.remove_widget(self.ids.slide_3)
        
        self.state = False

    def add(self, slide):
        self.ids.layout.remove_widget(self.ids.page_label)
        self.ids.layout.remove_widget(self.ids.btn_question_1)
        self.ids.layout.remove_widget(self.ids.btn_question_2)
        self.ids.layout.remove_widget(self.ids.btn_question_3)
        self.ids.layout.remove_widget(self.ids.btn_back)

        self.ids.layout.add_widget(slide)
        slide.load_slide(slide.slides[0])
        self.ids.layout.add_widget(self.ids.btn_back)

        self.state = True

    def remove(self):      
        self.ids.layout.remove_widget(self.ids.slide_1)
        self.ids.layout.remove_widget(self.ids.slide_2)
        self.ids.layout.remove_widget(self.ids.slide_3)

        self.ids.layout.add_widget(self.ids.btn_question_1)
        self.ids.layout.add_widget(self.ids.btn_question_2)
        self.ids.layout.add_widget(self.ids.btn_question_3)
        self.ids.layout.add_widget(self.ids.page_label)

        self.state = False
