from kivy.app import Widget
from kivy.graphics.svg import Svg
from kivy.uix.pagelayout import *
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang.builder import Builder


isLoggedIn = False
__loginInfo = {"RootAdmin": "RootProjectApple"}
"""
class LoginPage(Screen):
    def verify_credentials(self):
        if self.ids["login"].text == "username" and self.ids["passw"].text == "password":
            self.manager.current = "user"

class UserPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class FinalApp(App):
    def builder(self):
        return ScreenManagement

myApp = FinalApp()
myApp.run()

"""
def login(username, pwd):
    if (__loginInfo.__contains__(username)):
        if (__loginInfo.get(username) == pwd):
            return "Welcome Back " + username
        else:
            return "Invalid Login Credentials"
    else:
        return "Invalid Login Credentials"

class loginscreen():
    if (not isLoggedIn):
        pass
        # Lock them on this screen and Lock the menu
    else:
        pass

# Form for creating a new point event, Should create a event code
class page1():
    pass

# Barcode Scanner After event selection --> should display the event accessed based on code
class page2():
    pass

# Viewing a student's history record
class page3():
    pass

# Check History for an event --> Should last for 10 months
class page4():
    pass

class FinalApp(App):
    def build(self):
        return PageLayout()

myApp = FinalApp()
myApp.run()
