import kivy

from kivy.app import App
from kivy.uix.button import *
from kivy.uix.widget import *
from kivy.uix.floatlayout import *

# Sample 1:
'''
'''
class TestApp(App):
    def build(self):
        return Button()
TestApp().run()
'''
'''

'''
# Sample 2:
class CustomWidget(Widget):
    pass

class CustomWidgetApp(App):
    def build(self):
        return CustomWidget()
customWidget = CustomWidgetApp()
customWidget.run()
'''
# Sample 3:
class FloatingApp(App):
    def build(self):
        return FloatLayout()

flApp = FloatingApp()
flApp.run()