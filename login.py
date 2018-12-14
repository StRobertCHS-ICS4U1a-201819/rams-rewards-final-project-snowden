from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder

class LoginPage(Screen):
    def verify_credentials(self):
        if self.ids["login"].text == "username" and self.ids["passw"].text == "password":
            self.manager.current = "user"

class UserPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

kv_file = Builder.load_file('login.kv')

class LoginApp(App):
    def builder(self):
        return kv_file

if __name__ == '__main__':
    LoginApp().run()