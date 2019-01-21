# Basic Library
import random
import datetime

# Kivy App imports
from kivy.app import Widget
from kivy.app import App

# Kivy builder imports
from kivy.lang.builder import *
from kivy.lang import Builder

# Kivy core imports
from kivy.core.window import Window

# Kivy svg graphics import
from kivy.graphics.svg import Svg
from kivy.graphics import Color, Rectangle

# Python Kivy UIX imports
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.pagelayout import *
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput


isLoggedIn = False
loginInfo = {"": ""}
usedCodes = []
events = []
studentDB = {}

class Event(object):
    def __init__(self, points, eventType):
        self.points = points
        self.eventType = eventType
        self.title = ""

class customPopup(Popup):
    def returningValues(self, pointValue, eventType):
        myEvent = Event(pointValue, eventType)
        events.append(myEvent)

class Student(object):
    def __init__(self):
        self.activityNo = []
        self.points = 0

    def addActivity(self, activityCode, points):
        if (not self.activityNo.__contains__(activityCode)):
            self.activityNo.append(activityCode)
            self.points += points

stu1 = Student()
studentDB["0000000"] = stu1

class Teacher(object):
    def __init__(self, name):
        self.name = name

Builder.load_string("""
<LoginScreen>:
    username: login
    password: passw
    FloatLayout:
        pos_hint_y: 1
        pos_hint_x: 4.7
        TextInput:
            pos_hint: {"center_x": 0.6, "center_y": 0.75}
            id: login
            size_hint_x: 0.5
            size_hint_y: 0.05

        Label:
            text: "Username"
            pos_hint: {"center_x": 0.3, "center_y": 0.75}
            background_color: 0.5,0.5,0.5,0.8

        TextInput:
            id: passw
            pos_hint: {"center_x": 0.6, "center_y": 0.675}
            size_hint_x: .5
            size_hint_y: .05
            password: True # hide password

        Label:
            text: "Password"
            pos_hint: {"center_x": 0.3, "center_y": 0.675}

        CustButton:
            id: enter_credBtn
            pos_hint: {"center_x": 0.5, "center_y": .20}
            text: "Login"
            on_press:
                root.manager.transition.direction = "left"
                root.verify_credentials()

<EventScreen>:
    id: screen1
    popuptext: popupbtn
    FloatLayout:
        pos_hint_y: 1
        pos_hint_x: 4.7   
        
        Label:
            text: "Description:"
            pos_hint: {"center_x": 0.15, "center_y": 0.95}
            size_hint_y: 0.1
            
        TextInput:
            id: description
            pos_hint: {"center_x": 0.55, "center_y": 0.95}
            size_hint_x: 0.6
            size_hint_y: 0.05
        
        Button:
            id: popupbtn
            text: "Choose the activity type:"
            size_hint_x: .7
            pos_hint: {"center_x": 0.5, "center_y": 0.55}
            size_hint_y: 0.1
            on_press:
                root.open_event_choices()
            
        Button:
            text: "Create Event"
            pos_hint: {"center_x": 0.5, "center_y": 0.15}
            size_hint_y: 0.1
            on_press:
                app.root.current = "screen2"
            

<ScanScreen>:
    display: StuNoInput
    FloatLayout:
        TextInput:
            size_hint: 0.4, 0.05
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
            id: StuNoInput
        
        BoxLayout:
            size_hint: 0.8, 0.15
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
            Button:
                text: "1"
                on_press: StuNoInput.text += "1"
            Button:
                text: "2"
                on_press: StuNoInput.text += "2"
            Button:
                text: "3"
                on_press: StuNoInput.text += "3"
        
        BoxLayout:
            size_hint: 0.8, 0.15
            pos_hint: {"center_x": 0.5, "center_y": 0.45}
            Button:
                text: "4"
                on_press: StuNoInput.text += self.text
            Button:
                text: "5"
                on_press: StuNoInput.text += self.text
            Button:
                text: "6"
                on_press: StuNoInput.text += self.text
        
        BoxLayout:
            size_hint: 0.8, 0.15
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            Button:
                text: "7"
                on_press: StuNoInput.text += self.text
            Button:
                text: "8"
                on_press: StuNoInput.text += self.text
            Button:
                text: "9"
                on_press: StuNoInput.text += self.text
        
        BoxLayout:
            size_hint: 0.8, 0.15
            pos_hint: {"center_x": 0.5, "center_y": 0.15}
            Button:
                text: "CLR"
                on_press: StuNoInput.text = ""
            Button:
                text: "0"
                on_press: StuNoInput.text += self.text
            Button:
                text: "Bkspace"
                on_press: StuNoInput.text = StuNoInput.text[:-1]
            
        
        Button:
            text: "Add Points"
            size_hint: 0.8, 0.05
            pos_hint: {"center_x": 0.5, "center_y": 0.05}
            on_press: 
                root.add_points(StuNoInput)

<HistScreen>:
    Button:
        text: "Page 2"
        on_release: app.root.current = "user2"
    Button:
        text: "Page 4"
        on_release: app.root.current = "user4"

<Hist2Screen>:
    Button:
        text: "Page 3"
        on_release: app.root.current = "user3"

<CustButton@Button>:
    font_size: 30
    color: 0,0,0,1
    size: 150, 50
    background_normal: ''
    background_color: 0.8, 0.8, 0.8, 1
    size_hint: .5, .1
    
<CustomPopup>:
    display: ""
    pointValue: ""
    size_hint: .5, 1
    auto_dismiss: False
    title: "Choose the event:"
    FloatLayout:
        Button:
            text: "Attend a club"
            pos_hint: {"center_x": 0.5, "center_y": 0.95}
            size_hint_y: 0.1
            on_press:
                display = self.text
                pointValue = "25"
                root.dismiss()
        Button:
            text: "Attend Mass"
            pos_hint: {"center_x": 0.5, "center_y": 0.85}
            size_hint_y: 0.1
            on_press:
                display = self.text
                pointValue = "100"
                root.dismiss()
        Button:
            text: "Sharelife"
            pos_hint: {"center_x": 0.5, "center_y": 0.75}
            size_hint_y: 0.1
            on_press: 
                display = self.text
                pointValue = "1000"
                root.dismiss()
        
        Button:
            text: "Ram of the Month"
            pos_hint: {"center_x": 0.5, "center_y": 0.65}
            size_hint_y: 0.1
            on_press:
                display = self.text
                pointValue = "1000"
                root.dismiss()
        Button:
            text: "Other School Event"
            pos_hint: {"center_x": 0.5, "center_y": 0.55}
            size_hint_y: 0.1
            on_press:
                display = self.text
                pointValue = str(slider_id.value)
                root.dismiss()
        Slider:
            pos_hint: {"center_x": 0.5, "center_y": 0.45}
            size_hint_y: 0.1
            id: slider_id
            min: 0
            max: 1500
            value: 0
            step: 25
        Label:
            text: "Enter Custom Value: " + str(slider_id.value)
            pos_hint: {"center_x": 0.5, "center_y": 0.35}
            size_hint_y: 0.1
        Button:
            text: "Close"
            pos_hint: {"center_x": 0.5, "center_y": 0.25}
            size_hint_y: 0.1
            on_press: root.dismiss()
""")

# Basic login screen
class LoginScreen(Screen):
    def verify_credentials(self):
        print(self.username.text, self.password.text)
        if (loginInfo.__contains__(self.username.text)):
            if (loginInfo.get(self.username.text) == self.password.text):
                sm.current = "screen1"

# Form for creating a new point event, Should create a event code
class EventScreen(Screen):
    # Used to generate a 5 character code
    def code_Generate(self):
        chars = "ASDFGHJKLQWERTYUIOPZXCVBNM!@#$%^&*() {}:\"|<>?_~zxcvbnm,./asdfghjkl;\'\\]qwertyuiop[1234567890-+="
        code = ""
        for i in range(4):
            code += chars[random.randint(0, len(chars) - 1)]
        if (usedCodes.__contains__(code)):
            self.code_Generate()
        usedCodes.append(code)
        return code

    def open_event_choices(self):
        customPopup().open()

    def label_change(self, text):
        if text:
            self.popuptext.text = text

# Barcode Scanner After event selection --> should display the event accessed based on code
class ScanScreen(Screen):
    def add_points(self, stuNo, code, points):
        studentDB.get(stuNo).addActivity(code, points)

# Viewing a student's history record
class HistScreen(Screen):
    pass

# Check History for an event --> Should last for 1 day
class Hist2Screen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(LoginScreen(name="login"))
sm.add_widget(EventScreen(name="screen1"))
sm.add_widget(ScanScreen(name="screen2"))
sm.add_widget(HistScreen(name="screen3"))
sm.add_widget(Hist2Screen(name="screen4"))

class FinalApp(App):
    def build(self):
        Window.clearcolor = (34 / 255, 100 / 255, 34 / 255, 0.01)
        return sm

# Main Method
if __name__ == '__main__':
    FinalApp().run()

"""
Basic Template for making float layouts

pos_hint: {"center_x": 0.5, "center_y": 0.95}
            size_hint_y: 0.1
"""
