from kivy.app import App
from kivy.app import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.svg import Svg
from kivy.uix.pagelayout import *

isLoggedIn = False;
__loginInfo = {}
# Create a dictionary for username password combos

def login(username, pwd):
    pass

class loginscreen():
    if (not isLoggedIn):
        login("felix", 1234)
        # Lock them on this screen and Lock the menu
    else:
        pass

class page1():
    pass

class page2():
    pass

class page3():
    pass

class page4():
    pass

class FinalApp(App):
    def build(self):
        return PageLayout()

myApp = FinalApp()
myApp.run()