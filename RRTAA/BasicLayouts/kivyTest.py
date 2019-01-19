import kivy

from kivy.app import App
from kivy.uix.button import *
from kivy.uix.widget import *
from kivy.uix.floatlayout import *
from kivy.uix.gridlayout import *
from kivy.uix.boxlayout import *
from kivy.uix.stacklayout import *
from kivy.uix.pagelayout import *

# Sample 1:
'''
class TestApp(App):
    def build(self):
        return Button()
TestApp().run()
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
'''
# Sample 3:
class FloatingApp(App):
    def build(self):
        return FloatLayout()

flApp = FloatingApp()
flApp.run()
'''
'''
# Sample 4
class GridLayoutApp(App):
    def build(self):
        return GridLayout()

glApp = GridLayoutApp()
glApp.run()
'''
'''
# Sample 5
class BoxLayoutApp(App):
    def build(self):
        return BoxLayout()
    
blApp = BoxLayoutApp()
blApp.run()
'''
'''
# Sample 6
class StackLayoutApp(App):
    def build(self):
        return StackLayout()
slApp = StackLayoutApp()
slApp.run()
'''

# Sample 7
class PageLayoutApp(App):
    def build(self):
        return PageLayout()
plApp = PageLayoutApp()
plApp.run()