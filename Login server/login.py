import kivy
kivy.require('1.0.9')
from kivymd.app import MDApp
from kivy.lang import Builder
import mysql.connector as mysql
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

Window.size = (350, 580)

class LoginPage(MDApp):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        return screen_manager

    #def on_start(self):
        #Clock.schedule_once(self.login, 5)

    #def login(self, *args):
        #screen_manager.current = "login"


if __name__ == "__main__":
    LoginPage().run()

