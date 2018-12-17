# Kivy App imports
from kivy.app import Widget
from kivy.app import App

# Kivy builder import
from kivy.lang.builder import Builder

# Kivy svg graphics import
from kivy.graphics.svg import Svg

# Python Kivy UIX imports
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.pagelayout import *
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput


isLoggedIn = False
__loginInfo = {"Root": "Root2382"}
__studentDB = {1122365: 0}

def getSDB():
    return __studentDB

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Username:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Password:"))
        self.password = TextInput(multiline=False, password=True)
        self.add_widget(self.password)


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
        return LoginScreen()

myApp = FinalApp()
myApp.run()
