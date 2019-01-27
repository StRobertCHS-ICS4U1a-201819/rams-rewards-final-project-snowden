from kivy.app import App
from kivy.lang import Builder
from kivy.uix.pagelayout import PageLayout

loadstr = """
MyPageLayout:
    BoxLayout:
        canvas:
            Color:
                rgba: 216/255., 195/255., 88/255., 1
            Rectangle:
                pos: self.pos
                size: self.size
        orientation: 'vertical'
        Label:
            id: testid
            size_hint_y: None
            height: 1.5 * self.texture_size[1]
            text: 'student history'
        Button:
            id: scorebutton
            text: 'Please click to retrieve score!'
            #when pressed go to the retrieval score method
            on_press: root.retrievalscore()
            
            #on_press: print("student points")
           
           
            
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
            source: 'qrcode.50152115.png'
"""


class KivyTut2App(App):
#class KivyTut2App:
    def build(self):

        return Builder.load_string(loadstr)



#build new class to call retrieval score from PageLayout
class MyPageLayout(PageLayout):
    #pass
    def retrievalscore(self):
        #retrive score from text file
        linereadline = open("lookstudent/studentsite/scorefile.txt", "r")
        #display updated text from text file after user passes score
        keydisp = linereadline.readline() +' (click to retrieve score)'
        self.ids['scorebutton'].text =keydisp




sample_app = KivyTut2App()

sample_app.run()