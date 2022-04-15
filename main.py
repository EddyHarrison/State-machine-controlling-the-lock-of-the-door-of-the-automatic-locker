import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CourseWorkApp(App):
    status_label = None
    entry_text = None
    
    password = "1234"
    
    def processing(self, _):
        if self.entry_text.text == self.password:
            self.status_label.text = "Result: " + "Verified"
        else:
            self.status_label.text = "Result: " + "Authentication failure"
    
    def edit_text(self, _, value):
        if len(value) > 4:
            self.entry_text.text = value[len(value) - 4:]
        
        
    def build(self):
        box = BoxLayout(orientation='vertical')
        self.status_label = Label(text="Result: ")
        self.entry_text = TextInput()
        button_result = Button(text="Solve")
        
        self.status_label.bind(size=self.status_label.setter('text_size')) 
        self.halign = "right"
        self.valign = "middle"
        
        button_result.bind(on_press=self.processing)
        self.entry_text.bind(text=self.edit_text)
        
        box.add_widget(self.status_label)
        box.add_widget(self.entry_text)
        box.add_widget(button_result)
        
        return box

def main():
    CourseWorkApp().run()

if __name__ == "__main__":
    main()
 
