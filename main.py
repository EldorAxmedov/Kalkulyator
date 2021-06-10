from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class CalculyatorApp(App):
    def update_label(self):
        self.lbl.text = self.formula
    def add_number(self, instance):
        if self.formula=="0":
            self.formula=""
        self.formula += str(instance.text)
        self.update_label()
    def add_operation(self, instance):
        self.formula += str(instance.text)
        self.update_label()
    def calc_result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = "0"

    def reset(self, instance):
        self.formula = "0"
        self.update_label()
    def build(self):
        self.formula = "0"
        bl=BoxLayout(orientation='vertical', padding=25)
        gl=GridLayout(cols=4, spacing=3, size_hint=(1, .6))

        self.lbl=Label(text="0", font_size=40, halign="right", valign="center", size_hint=(1, .4))
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='7', on_press=self.add_number))
        gl.add_widget(Button(text='8', on_press=self.add_number))
        gl.add_widget(Button(text='9', on_press=self.add_number))
        gl.add_widget(Button(text='*', on_press=self.add_operation))

        gl.add_widget(Button(text='6', on_press=self.add_number))
        gl.add_widget(Button(text='5', on_press=self.add_number))
        gl.add_widget(Button(text='4', on_press=self.add_number))
        gl.add_widget(Button(text='+', on_press=self.add_operation))

        gl.add_widget(Button(text='3', on_press=self.add_number))
        gl.add_widget(Button(text='2', on_press=self.add_number))
        gl.add_widget(Button(text='1', on_press=self.add_number))
        gl.add_widget(Button(text='-', on_press=self.add_operation))

        gl.add_widget(Button(text='0', on_press=self.add_number))
        gl.add_widget(Button(text='=', on_press=self.calc_result))
        gl.add_widget(Button(text='С', on_press=self.reset))
        gl.add_widget(Button(text='/', on_press=self.add_operation))
        bl.add_widget(gl)
        return bl
if __name__ =="__main__":
    CalculyatorApp().run()