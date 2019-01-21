from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string("""
PageLayout:
    BoxLayout:

        canvas:
            Color:
                rgba: 216/255., 195/255., 88/255., 1
            Rectangle:
                pos: self.pos
                size: self.size
        orientation: 'vertical'
        Label:
            size_hint_y: None
            height: 1.5 * self.texture_size[1]
            text: 'student history'
        Button:
            text: 'points'
            on_press: print("student points")
    BoxLayout:
        orientation: 'vertical'
        canvas:
            Color:
                rgba: 109/255., 8/255., 57/255., 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: 'Dong'
        Label:
            text: 'Connor'
        Label: 
            text: 'student id' 
        Label: 
            text: 'homeroom'

    BoxLayout:
        canvas:
            Color:
                rgba: 37/255., 39/255., 30/255., 1
            Rectangle:
                pos: self.pos
                size: self.size
        cols: 1
        Button:
            text: '0000000'
            on_press: print("test")
        AsyncImage:
            source: 'https://i.redd.it/lr720nuui4z11.png'
""")


class KivyTut2App(App):
    def build(self):
        return root


sample_app = KivyTut2App()

sample_app.run()
