from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup



class Result_popup(Popup):
    def answers(self, bmi):
        if bmi < 18.5:
            self.ids.bmi_number.text = "BMI number "+str(bmi)
            self.ids.result.text = "Your status is: Underweight"
        elif bmi < 24.9:
            self.ids.bmi_number.text = "BMI number "+str(bmi)
            self.ids.result.text = "Your status is: Normal"
        elif bmi < 29.9:
            self.ids.bmi_number.text = "BMI number "+str(bmi)
            self.ids.result.text = "Your status is: Overweight"
        else:
            self.ids.bmi_number.text = "BMI number "+str(bmi)
            self.ids.result.text = "Your status is: Obese"
        self.open()

class Error_popup(Popup):
    def reason(self, reason):
        self.ids.reason.text = reason
        self.open()

class Main_grid(GridLayout):

    def get_bmi(self):
        height = float(self.ids.height.text) / 100 # this is to convert cm to m
        weight = float(self.ids.weight.text)
        bmi = weight / (height ** 2)
        return bmi
    
    def check_bmi(self):
        if self.ids.height.text == "" or self.ids.weight.text == "" or self.ids.height.text == "0" or self.ids.weight.text == "0":
            err_pop = Error_popup()
            err_pop.reason("Please enter valid values")
            return False
        return True
    
    def calculate_bmi(self):
        check_BMi = self.check_bmi()
        if check_BMi:
            bmi = self.get_bmi()
            #print(bmi)
            res_pop = Result_popup()
            res_pop.answers(bmi)







class BMI_CalculatorApp(App):
    def build(self):
        return Main_grid()
    
if __name__ == "__main__":
    BMI_CalculatorApp().run()