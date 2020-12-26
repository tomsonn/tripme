#!/usr/bin/env python3

import re

import kivy
kivy.require('2.0.0')

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import NoTransition
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, ColorProperty
from kivy.lang import Builder
from kivy.app import App
from kivy.utils import get_color_from_hex


EMAIL_DEFAULT = 'Type your Email'
PASSWORD_DEFAULT = 'Type your Password'
USERNAME_DEFAULT = 'Type your Username'
DEPT_PLACE_DEFAULT = 'Type your departure place'
ARRIVAL_DEST_DEFAULT = 'Type your arrival destination'
DATE_DEFAULT = 'DD/MM/YYYY'

colors = {
    'paletteWhite': get_color_from_hex('FFFFFF'),
    'paletteCloudLight': get_color_from_hex('#F5F7F9'),
    'paletteProductNormal': get_color_from_hex('#00A991'),
    'paletteProductDark': get_color_from_hex('#007F6D'),
    'paletteBlack': get_color_from_hex('#000000'),
    'paletteInkLight': get_color_from_hex('#5F738C'),
    'paletteInkNormal': get_color_from_hex('#252A31'),
    'paletteTextPrimary': get_color_from_hex('#252A31'),
    'paletteBlueNormal': get_color_from_hex('#0172CB'),
    'paletteBlueLight': get_color_from_hex('#E8F4FD'),
    'paletteRedDark': get_color_from_hex('#970C0C'),
    'paletteRedNormal': get_color_from_hex('#D21C1C'),
    'paletteOrangeDark': get_color_from_hex('#A25100'),
    'paletteOrangeNormal': get_color_from_hex('#E98305')
}


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        login_email = ObjectProperty()
        login_password = ObjectProperty()

    def on_touch_up(self, touch):
        """Decide wheter user touched desired field or not"""

        if self.ids.login_email.collide_point(*touch.pos):
            self.pressed_input(type_='email')
            self.ids.login_email.default_color = False
            return True
        
        if self.ids.login_password.collide_point(*touch.pos):
            self.pressed_input(type_='password')
            self.ids.login_password.default_color = False
            return True
        
        return super(LoginScreen, self).on_touch_up(touch)

    def pressed_input(self, type_):
        """Once there is a focus on field, clear default text"""

        if type_ == 'email':
            if self.login_email.text == EMAIL_DEFAULT:
                self.login_email.text = ''
        elif type_ == 'password':
            if self.login_password.text == PASSWORD_DEFAULT:
                self.login_password.text = ''
        else:
            raise ValueError('Bad input parameter.')

    def init_form(self):
        """Reset form text"""

        self.login_email.text = EMAIL_DEFAULT
        self.login_password.text = PASSWORD_DEFAULT

        self.login_email.default_color = True
        self.login_password.default_color = True

    def proceed_to_create_acc_screen(self):
        """Change current screen to `createAccount` and reset form text"""

        screen_manager.current = 'createAccount'
        self.init_form()

    def proceed_to_search_screen(self):
        """Change current screen to `search` and reset form text"""

        screen_manager.current = 'search'
        self.init_form()


class CreateAccountScreen(Screen):

    def __init__(self, **kwargs):
        super(CreateAccountScreen, self).__init__(**kwargs)

        # Load properties
        create_acc_email = ObjectProperty()
        create_acc_password = ObjectProperty()
        create_acc_username = ObjectProperty()

    def on_touch_up(self, touch):
        """Decide wheter user touched desired field or not"""

        if self.ids.create_acc_email.collide_point(*touch.pos):
            self.pressed_input(type_='email')
            self.ids.create_acc_email.default_color = False
            return True
        
        if self.ids.create_acc_password.collide_point(*touch.pos):
            self.pressed_input(type_='password')
            self.ids.create_acc_password.default_color = False
            return True
        
        if self.ids.create_acc_username.collide_point(*touch.pos):
            self.pressed_input(type_='username')
            self.ids.create_acc_username.default_color = False
            return True
        
        return super(CreateAccountScreen, self).on_touch_up(touch)

    def pressed_input(self, type_):
        """Once there is a focus on field, clear default text"""

        if type_ == 'email':
            if self.create_acc_email.text == EMAIL_DEFAULT:
                self.create_acc_email.text = ''
        elif type_ == 'password':
            if self.create_acc_password.text == PASSWORD_DEFAULT:
                self.create_acc_password.text = ''
        elif type_ == 'username':
            if self.create_acc_username.text == USERNAME_DEFAULT:
                self.create_acc_username.text = ''
        else:
            raise ValueError('Bad input parameter.')

    def clear_form(self):
        """Clear form fields"""

        self.create_acc_email.text = ''
        self.create_acc_password.text = ''
        self.create_acc_username.text = ''

    def init_form(self):
        """Reset form text"""

        self.create_acc_email.text = EMAIL_DEFAULT
        self.create_acc_password.text = PASSWORD_DEFAULT
        self.create_acc_username.text = USERNAME_DEFAULT

        self.create_acc_email.default_color = True
        self.create_acc_password.default_color = True
        self.create_acc_username.default_color = True

    def proceed_to_login_screen(self):
        """Change current screen to `login` and reset form text"""

        screen_manager.current = 'login'
        self.init_form()


class SearchScreen(Screen):
    
    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)

        dept_place = ObjectProperty()
        dept_date = ObjectProperty()
        arr_dest = ObjectProperty()

    def on_touch_up(self, touch):
        """Decide wheter user touched desired field or not"""

        if self.ids.dept_place.collide_point(*touch.pos):
            self.pressed_input(type_='dept_place')
            self.ids.dept_place.default_color = False
            self.ids.dept_place.is_empty = False
            return True
        
        if self.ids.arr_dest.collide_point(*touch.pos):
            self.pressed_input(type_='arr_dest')
            self.ids.arr_dest.default_color = False
            self.ids.arr_dest.is_empty = False
            return True

        if self.ids.dept_date.collide_point(*touch.pos):
            self.pressed_input(type_='dept_date')
            self.ids.dept_date.default_color = False
            self.ids.dept_date.invalid_format = False
            return True
        
        return super(SearchScreen, self).on_touch_up(touch)

    def pressed_input(self, type_):
        """Once there is a focus on field, clear default text"""

        if type_ == 'dept_place':
            if self.dept_place.text == DEPT_PLACE_DEFAULT:
                self.dept_place.text = ''
        elif type_ == 'arr_dest':
            if self.arr_dest.text == ARRIVAL_DEST_DEFAULT:
                self.arr_dest.text = ''
        elif type_ == 'dept_date':
            if self.dept_date.text == DATE_DEFAULT:
                self.dept_date.text = ''
        else:
            raise ValueError('Bad input parameter.')

    def parse_date(self, date):
        date_pattern = r'(\d{2})/(\d{2})/(\d{4})'
        matches = re.search(date_pattern, date)

        if matches and len(matches.groups()) == 3:
            return {
                'day': matches.group(1),
                'month': matches.group(2),
                'year': matches.group(3)
            }
        else:
            self.dept_date.invalid_format = True
            self.dept_date.text = ''

            return {}

    def validate_inputs(self):
        invalid_inputs = ['', DEPT_PLACE_DEFAULT, ARRIVAL_DEST_DEFAULT]
        if self.dept_place.text in invalid_inputs:
            self.dept_place.is_empty = True

        if self.arr_dest.text in invalid_inputs:
            self.arr_dest.is_empty = True

    def clear_form(self):
        """Clear form fields"""

        self.dept_place.text = ''
        self.arr_dest.text = ''
        self.dept_date.text = ''

        self.dept_place.is_empty = False
        self.arr_dest.is_empty = False
        self.dept_date.invalid_format = False

    def init_form(self):
        self.dept_place.text = DEPT_PLACE_DEFAULT
        self.arr_dest.text = ARRIVAL_DEST_DEFAULT
        self.dept_date.text = DATE_DEFAULT

        self.dept_place.is_empty = False
        self.arr_dest.is_empty = False
        self.dept_date.invalid_format = False


class ResultsScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


# Load kivy style file in case kivy can not find it internally
kv = Builder.load_file('tripme.kv')

screen_manager = WindowManager(transition=NoTransition())
screens = [LoginScreen(name='login'),
            CreateAccountScreen(name='createAccount'),
            SearchScreen(name='search'),
            ResultsScreen(name='results')]
for screen in screens:
    screen_manager.add_widget(screen)

screen_manager.current = 'login'


class TripmeApp(App):
    title = 'TripMe'

    def build(self):
        return screen_manager


if __name__ == '__main__':
    TripmeApp().run()
