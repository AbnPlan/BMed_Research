
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
import db_manager as db

class MenuScreen(Screen):
    '''Main menu screen'''
    pass

class EntryForm(Screen):
    '''Entry form screen'''
    def clear_text(self):
        '''Clear all textboxes'''
        self.ids.ef_full_name.text = ''
        self.ids.phone_number.text = ''
        self.ids.address_line1.text = ''
        self.ids.address_line2.text = ''
        self.ids.town.text = ''
        self.ids.country.text = 'Puerto Rico'
        self.ids.zip_code.text = ''
        self.ids.health_insurance.text = ''
        self.ids.other.state = 'down'

    def save_form(self):
        '''Save form into Database'''
        db_connection = db.db_connection()

        if self.ids.tripleS.state == 'down':
            h_i = 'Triple S'
        elif self.ids.reforma.state == 'down':
            h_i = 'Reforma'
        elif self.ids.mcs.state == 'down':
            h_i = 'MCS'
        elif self.ids.humana.state == 'down':
            h_i = 'Humana'
        else:
            h_i = self.ids.health_insurance.text

        db.insert_patient(
            db_connection, 
            self.ids.ef_full_name.text,
            self.ids.phone_number.text,
            self.ids.address_line1.text,
            self.ids.address_line2.text,
            self.ids.town.text,
            self.ids.country.text,
            self.ids.zip_code.text,
            h_i
        )

        db_connection.close()
    
    def show_popup(self):
        if (
            self.ids.ef_full_name.text=='' or
            self.ids.phone_number.text=='' or
            self.ids.address_line1.text=='' or
            self.ids.town.text=='' or
            self.ids.country.text=='' or
            self.ids.zip_code.text=='' or
            (self.ids.health_insurance.text == '' and self.ids.other.state == 'down') or
            (self.ids.other.state == 'normal' and self.ids.tripleS.state == 'normal' and 
            self.ids.reforma.state == 'normal' and self.ids.mcs.state == 'normal' and 
            self.ids.humana.state == 'normal')
            ):
            show = Fail()
            popup_window = Popup(title='', content=show, size_hint=(0.30, 0.20))
            popup_window.open()
            return False

        show = Success()
        popup_window = Popup(title='', content=show, size_hint=(0.30, 0.20))
        popup_window.open()
        return True

class Appointments(Screen):
    '''APPOINTMENTS SCREEN'''
    def show_popup(self):
        if (
            (self.ids.fiebre_no.state == 'normal' and self.ids.fiebre_yes.state == 'normal') or
            (self.ids.tos_no.state == 'normal' and self.ids.tos_yes.state == 'normal') or
            (self.ids.diff_resp_no.state == 'normal' and self.ids.diff_resp_yes.state == 'normal') or
            (self.ids.escalofrios_no.state == 'normal' and self.ids.escalofrios_yes.state == 'normal') or
            (self.ids.temblores_no.state == 'normal' and self.ids.temblores_yes.state == 'normal') or
            (self.ids.dolor_muscular_no.state == 'normal' and self.ids.dolor_muscular_yes.state == 'normal') or
            (self.ids.dolor_cabeza_no.state == 'normal' and self.ids.dolor_cabeza_yes.state == 'normal') or
            (self.ids.dolor_garganta_no.state == 'normal' and self.ids.dolor_garganta_yes.state == 'normal') or
            (self.ids.perdida_olfato_gusto_no.state == 'normal'and self.ids.perdida_olfato_gusto_yes.state == 'normal') or
            (self.ids.service1.state == 'normal' and self.ids.service2.state == 'normal') or
            (self.ids.urgency_lvl1.state == 'normal' and self.ids.urgency_lvl2.state == 'normal' and
             self.ids.urgency_lvl3.state == 'normal' and self.ids.urgency_lvl4.state == 'normal' and
             self.ids.urgency_lvl5.state == 'normal') or 
            (self.ids.a_full_name.text == '')
            ):
            show = Fail()
            popup_window = Popup(title='', content=show, size_hint=(0.30, 0.20))
            popup_window.open()
            return False

        show = Success()
        popup_window = Popup(title='', content=show, size_hint=(0.30, 0.20))
        popup_window.open()
        return True

    def clear(self):
        self.ids.fiebre_no.state = 'down'
        self.ids.tos_no.state = 'down'
        self.ids.diff_resp_no.state = 'down'
        self.ids.escalofrios_no.state = 'down'
        self.ids.temblores_no.state = 'down'
        self.ids.dolor_muscular_no.state = 'down'
        self.ids.dolor_cabeza_no.state = 'down'
        self.ids.dolor_garganta_no.state = 'down'
        self.ids.perdida_olfato_gusto_no.state = 'down'
        self.ids.urgency_lvl1.state = 'down'
        self.ids.service2.state = 'down'
        self.ids.a_full_name.text = ''
    
    def save_form(self):
        '''Save form into Database'''
        db_connection = db.db_connection()

        if self.ids.urgency_lvl1.state == 'down':
            u_l = 1
        elif self.ids.urgency_lvl2.state == 'down':
            u_l = 2
        elif self.ids.urgency_lvl3.state == 'down':
            u_l = 3
        elif self.ids.urgency_lvl4.state == 'down':
            u_l = 4
        else:
            u_l = 5

        if self.ids.service2.state == 'down':
            service = 'Pediatria'
        else:
            service = 'Sala de Emergencias'

        Fiebre = 'No'
        Tos = 'No'
        DiffResp = 'No'
        Escalofrios = 'No'
        Temblores = 'No'
        DolorMuscular = 'No'
        DolorCabeza = 'No'
        DolorGarganta = 'No'
        PerdidaOlfatoGusto = 'No'

        if self.ids.fiebre_yes.state == 'down':
            Fiebre = 'Yes'
        if self.ids.tos_yes.state == 'down':
            Tos = 'Yes'
        if self.ids.diff_resp_yes.state == 'down':
            DiffResp = 'Yes'
        if self.ids.escalofrios_yes.state == 'down':
            Escalofrios = 'Yes'
        if self.ids.temblores_yes.state == 'down':
            Temblores = 'Yes'
        if self.ids.dolor_muscular_yes.state == 'down':
            DolorMuscular = 'Yes'
        if self.ids.dolor_cabeza_yes.state == 'down':
            DolorCabeza = 'Yes'
        if self.ids.dolor_garganta_yes.state == 'down':
            DolorGarganta = 'Yea'
        if self.ids.perdida_olfato_gusto_yes.state == 'down':
            PerdidaOlfatoGusto = 'Yes'

        db.insert_appointment(
            db_connection,
            self.ids.a_full_name.text,
            u_l,
            service,
            Fiebre,
            Tos,
            DiffResp,
            Escalofrios,
            Temblores,
            DolorMuscular,
            DolorCabeza,
            DolorGarganta,
            PerdidaOlfatoGusto
        )

        db_connection.close()

class Survey(Screen):
    '''Survey screen'''
    def clear_screen(self):
        self.ids.q_0_0.state = 'down'
        self.ids.q_1_0.state = 'down'
        self.ids.q_2_0.state = 'down'
        self.ids.q_3_0.state = 'down'
        self.ids.comments.text = ''
        self.ids.rating_quality_1.state = 'down'
        self.ids.rating_visual_1.state = 'down'
        self.ids.rating_user_friendly_1.state = 'down'
        self.ids.rating_functionality_1.state = 'down'
        self.ids.improvement_size_1.state = 'down'
        self.ids.improvement_functionality_1.state = 'down'
        self.ids.improvement_quality_1.state = 'down'
        self.ids.scrollview.scroll_y = 1

    def save_survey(self):
        '''Save form into Database'''
        db_connection = db.db_connection()

        if self.ids.q_0_0.state == 'down':
            q0 = 1
        elif self.ids.q_0_1.state == 'down':
            q0 = 2
        elif self.ids.q_0_2.state == 'down':
            q0 = 3
        elif self.ids.q_0_3.state == 'down':
            q0 = 4
        elif self.ids.q_0_4.state == 'down':
            q0 = 5
        
        if self.ids.q_1_0.state == 'down':
            q1 = 1
        elif self.ids.q_1_1.state == 'down':
            q1 = 2
        elif self.ids.q_1_2.state == 'down':
            q1 = 3
        elif self.ids.q_1_3.state == 'down':
            q1 = 4
        
        if self.ids.q_2_0.state == 'down':
            q2 = 1
        elif self.ids.q_2_1.state == 'down':
            q2 = 2
        elif self.ids.q_2_2.state == 'down':
            q2 = 3
        elif self.ids.q_2_3.state == 'down':
            q2 = 4
        
        if self.ids.q_3_0.state == 'down':
            q3 = 1
        elif self.ids.q_3_1.state == 'down':
            q3 = 2
        elif self.ids.q_3_2.state == 'down':
            q3 = 3
        elif self.ids.q_3_3.state == 'down':
            q3 = 4
        
        q4 = self.ids.comments.text

        if self.ids.rating_quality_1.state == 'down':
            rating_quality = 1
        elif self.ids.rating_quality_2.state == 'down':
            rating_quality = 2
        elif self.ids.rating_quality_3.state == 'down':
            rating_quality = 3
        elif self.ids.rating_quality_4.state == 'down':
            rating_quality = 4
        
        if self.ids.rating_visual_1.state == 'down':
            rating_visual = 1
        elif self.ids.rating_visual_2.state == 'down':
            rating_visual = 2
        elif self.ids.rating_visual_3.state == 'down':
            rating_visual = 3
        elif self.ids.rating_visual_4.state == 'down':
            rating_visual = 4
        
        if self.ids.rating_user_friendly_1.state == 'down':
            rating_user_friendly = 1
        elif self.ids.rating_user_friendly_2.state == 'down':
            rating_user_friendly = 2
        elif self.ids.rating_user_friendly_3.state == 'down':
            rating_user_friendly = 3
        elif self.ids.rating_user_friendly_4.state == 'down':
            rating_user_friendly = 4
        
        if self.ids.rating_functionality_1.state == 'down':
            rating_functionality = 1
        elif self.ids.rating_functionality_2.state == 'down':
            rating_functionality = 2
        elif self.ids.rating_functionality_3.state == 'down':
            rating_functionality = 3
        elif self.ids.rating_functionality_4.state == 'down':
            rating_functionality = 4

        if self.ids.improvement_size_1.state == 'down':
            improvement_size = 1
        elif self.ids.improvement_size_2.state == 'down':
            improvement_size = 2
        elif self.ids.improvement_size_3.state == 'down':
            improvement_size = 3

        if self.ids.improvement_functionality_1.state == 'down':
            improvement_functionality = 1
        elif self.ids.improvement_functionality_2.state == 'down':
            improvement_functionality = 2
        elif self.ids.improvement_functionality_3.state == 'down':
            improvement_functionality = 3
        
        if self.ids.improvement_quality_1.state == 'down':
            improvement_quality = 1
        elif self.ids.improvement_quality_2.state == 'down':
            improvement_quality = 2
        elif self.ids.improvement_quality_3.state == 'down':
            improvement_quality = 3
        
        db.insert_survey(db_connection, q0, q1, q2, q3, q4,
                        rating_quality, rating_visual, rating_user_friendly,
                        rating_functionality, improvement_size, improvement_functionality, 
                        improvement_quality)
        db_connection.close()

    def show_popup(self):
        if (
            (self.ids.q_0_0.state == 'normal' and
            self.ids.q_0_1.state == 'normal' and
            self.ids.q_0_2.state == 'normal' and
            self.ids.q_0_3.state == 'normal' and
            self.ids.q_0_4.state == 'normal') or
            (self.ids.q_1_0.state == 'normal' and
            self.ids.q_1_1.state == 'normal' and
            self.ids.q_1_2.state == 'normal' and
            self.ids.q_1_3.state == 'normal') or
            (self.ids.q_2_0.state == 'normal' and
            self.ids.q_2_1.state == 'normal' and
            self.ids.q_2_2.state == 'normal' and
            self.ids.q_2_3.state == 'normal') or
            (self.ids.q_3_0.state == 'normal' and
            self.ids.q_3_1.state == 'normal' and
            self.ids.q_3_2.state == 'normal' and
            self.ids.q_3_3.state == 'normal') or
            (self.ids.rating_quality_1.state == 'normal' and
            self.ids.rating_quality_2.state == 'normal' and
            self.ids.rating_quality_3.state == 'normal' and
            self.ids.rating_quality_4.state == 'normal') or
            (self.ids.rating_visual_1.state == 'normal' and
            self.ids.rating_visual_2.state == 'normal' and
            self.ids.rating_visual_3.state == 'normal' and
            self.ids.rating_visual_4.state == 'normal') or
            (self.ids.rating_user_friendly_1.state == 'normal' and
            self.ids.rating_user_friendly_2.state == 'normal' and
            self.ids.rating_user_friendly_3.state == 'normal' and
            self.ids.rating_user_friendly_4.state == 'normal') or
            (self.ids.rating_functionality_1.state == 'normal' and
            self.ids.rating_functionality_2.state == 'normal' and
            self.ids.rating_functionality_3.state == 'normal' and
            self.ids.rating_functionality_4.state == 'normal') or
            (self.ids.improvement_size_1.state == 'normal' and
            self.ids.improvement_size_2.state == 'normal' and
            self.ids.improvement_size_3.state == 'normal') or
            (self.ids.improvement_functionality_1.state == 'normal' and
            self.ids.improvement_functionality_2.state == 'normal' and
            self.ids.improvement_functionality_3.state == 'normal') or
            (self.ids.improvement_quality_1.state == 'normal' and
            self.ids.improvement_quality_2.state == 'normal' and
            self.ids.improvement_quality_3.state == 'normal')
        ):
            show = Fail()
            popup_window = Popup(title='', content=show, size_hint=(0.30, 0.20))
            popup_window.open()
            return 0

        show = Success()
        popup_window = Popup(title='', content=show, size_hint=(0.30, 0.20))
        popup_window.open()
        return 1



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

class Fail(FloatLayout):
    pass

class Success(FloatLayout):
    pass
