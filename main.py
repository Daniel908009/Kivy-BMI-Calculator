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
        height = float(self.ids.height.text)
        weight = float(self.ids.weight.text)
        if self.system == "Metric":
            height = height/100 # this is to convert cm to m
            bmi = weight / (height ** 2)
        else:
            bmi = 703 * (weight / (height ** 2))
        return round(bmi, 2)
    
    def check_bmi(self):
        if self.system == "Metric":
            if self.ids.height.text == "" or self.ids.weight.text == "" or self.ids.height.text <= "122" or self.ids.height.text >= "300" or self.ids.weight.text <= "1" or self.ids.weight.text >= "300":
                err_pop = Error_popup()
                err_pop.reason("Please enter valid values")
                return False
            else:
                return True
        else:
            if self.ids.height.text == "" or self.ids.weight.text == "" or self.ids.height.text >= "96" or self.ids.height.text <= "48" or self.ids.weight.text >= "700" or self.ids.weight.text <= "40":
                err_pop = Error_popup()
                err_pop.reason("Please enter valid values")
                return False
            else:
                return True
    
    def calculate_bmi(self):
        check_BMi = self.check_bmi()
        if check_BMi:
            bmi = self.get_bmi()
            #print(bmi)
            res_pop = Result_popup()
            res_pop.answers(bmi)

    def switch_system(self):
        if self.system == "Metric":
            self.system = "Imperial"
            self.ids.system_label.text = "Switch system, current: %s" % self.system
            self.ids.height_label.text = "Height (in) max: 96, min: 48"
            self.ids.weight_label.text = "Weight (lbs) max: 700, min 40"
        else:
            self.system = "Metric"
            self.ids.system_label.text = "Switch system, current: %s" % self.system
            self.ids.height_label.text = "Height (cm) max: 300, min: 122"
            self.ids.weight_label.text = "Weight (kg) max: 300, min: 1"

    def switch_advanced(self):
        if self.advanced == "False":
            self.advanced = "True"
            self.ids.advanced_label.text = "Advanced form, current: %s" % self.advanced
        else:
            self.advanced = "False"
            self.ids.advanced_label.text = "Advanced form, current: %s" % self.advanced






class BMI_CalculatorApp(App):
    def build(self):
        return Main_grid()
    
if __name__ == "__main__":
    BMI_CalculatorApp().run()