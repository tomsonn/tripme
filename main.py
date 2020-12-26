#!/usr/bin/env python3

import kivy
kivy.require('2.0.0')

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, ColorProperty
from kivy.lang import Builder
from kivy.app import App
from kivy.utils import get_color_from_hex


EMAIL_DEFAULT = 'Type your Email'
PASSWORD_DEFAULT = 'Type your Password'
USERNAME_DEFAULT = 'Type your Username'

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
        if type_ == 'email':
            if self.login_email.text == EMAIL_DEFAULT:
                self.login_email.text = ''
        elif type_ == 'password':
            if self.login_password.text == PASSWORD_DEFAULT:
                self.login_password.text = ''
        else:
            raise ValueError('Bad input parameter.')

    def proceed_to_create_acc_page(self):
        screen_manager.current = 'createAccount'

        self.login_email.text = EMAIL_DEFAULT
        self.login_password.text = PASSWORD_DEFAULT

        self.login_email.default_color = True
        self.login_password.default_color = True


class CreateAccountScreen(Screen):

    def __init__(self, **kwargs):
        super(CreateAccountScreen, self).__init__(**kwargs)

        create_acc_email = ObjectProperty()
        create_acc_password = ObjectProperty()
        create_acc_username = ObjectProperty()

    def on_touch_up(self, touch):
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
        self.create_acc_email.text = ''
        self.create_acc_password.text = ''
        self.create_acc_username.text = ''

    def proceed_to_login_page(self):
        screen_manager.current = 'login'
        self.create_acc_email.text = EMAIL_DEFAULT
        self.create_acc_password.text = PASSWORD_DEFAULT
        self.create_acc_username.text = USERNAME_DEFAULT

        self.create_acc_email.default_color = True
        self.create_acc_password.default_color = True
        self.create_acc_username.default_color = True


class SearchScreen(Screen):
    
    def proceed_to_login(self):
        screen_manager.current = 'login'


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
