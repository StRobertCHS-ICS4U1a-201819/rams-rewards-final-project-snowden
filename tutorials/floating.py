import kivy
kivy.require('1.9.0')


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


# A Float layout positions and sizes objects as a percentage
# of the window size

class FloatingApp(App):

    def build(self):
        return FloatLayout()


flApp = FloatingApp()

flApp.run()