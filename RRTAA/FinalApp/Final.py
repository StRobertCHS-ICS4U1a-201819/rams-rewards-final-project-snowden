from kivy.app import *
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.svg import Svg
from kivy.uix.pagelayout import *

"""
class QrCodeGen():
    pass
"""

class page1():
    pass

class page2():
    pass

class page3():
    pass

class page4():
    pass

class FinalLayout():
    pass

class FinalApp(App):
    def build(self):
        return FinalLayout()

"""
class QrCodeGenApp(App):
    def build(self):
        return QrCodeGen()

a = QrCodeGenApp()
a.run()
"""
myApp = FinalApp()
myApp.run()