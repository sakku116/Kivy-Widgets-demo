from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

# set window size
#Window.size = (500, 500)
# load kv design file 
Builder.load_file('basic.kv')

class MyGridLayout(Widget):
    checked = []
    def checkbox_click(self, instance, value, string): # self, instance, value adalah parameter utama
        if value == True:
            MyGridLayout.checked.append(string)
            self.ids.cb_label_output.text = f'string: {MyGridLayout.checked}'
        else:
            MyGridLayout.checked.remove(string)
            self.ids.cb_label_output.text = f'string: {MyGridLayout.checked}'

    def submit_press(self):
        get_input_text = self.ids.basic_textinput.text
        self.ids.basic_label.text = get_input_text

    def slider_slided(self, *args):
        value = str(int(args[1])) # args merupakan list, ambil index 1 untuk value (int)
        self.ids.slider_label.text = f'font size: {value}'
        self.ids.slider_label.font_size = int(value)
        
# main APP / build the window
class MyFirstApp(App):
    def build(self):
        return MyGridLayout()
# i dont know this works but this code is to run the kivy app
if __name__ == '__main__':
    MyFirstApp().run()

