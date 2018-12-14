from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton


class StudentListButton(ListItemButton):
    pass


class StudentDB(BoxLayout):
    # Connects the value in the TextInput widget to these
    # fields
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    student_list = ObjectProperty()

    def submit_student(self):
        pass

    def delete_student(self, *args):
        pass


    def replace_student(self, *args):
        pass



class StudentDBApp(App):
    def build(self):
        return StudentDB()


dbApp = StudentDBApp()

dbApp.run()