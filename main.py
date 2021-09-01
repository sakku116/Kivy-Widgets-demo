# "C:\py venv\kivy_venv\activate\scripts"

from kivy.app import App
#from kivy.uix.widget import Widget # untuk penggunaan regular
from kivy.uix.tabbedpanel import TabbedPanel # untuk penggunaan panel tab
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.lang import Builder

# set window size
Window.size = (500, 500)

# load kv design file
Builder.load_file('basic_widgets.kv')

class MyGridLayout(TabbedPanel):
    # ganti parameter antara Widget(untuk penggunaan regular sebagai layout screen,
    # gunakan GridLayout/BoxLayout untuk container utama)
    # atau TabbedPanel(untuk penggunaan panel tab sebagai container utama)
    # jika menggunakan tabbedpanel, maka untuk membuat main layout
    # menggunakan TabbedPanelItem disamping menggunakan gridlayout, boxlayout dll

    checked = []

    def checkbox_click(self, instance, value, string): # ( self, instance, value adalah parameter utama )
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
        # args berisikan list, ambil index 1 untuk mengambil value(int)
        value = str(int(args[1]))

        self.ids.slider_label.text = f'font size: {value}'
        self.ids.slider_label.font_size = int(value)

    def spinner_clicked(self, value):
        self.ids.spinner_label.text = f'you picked: {value}'

    def animate_widget(self, widget, *args): # (self, widget adalah parameter utama)
        # (widget adalah target widget pemanggil)

        animate = Animation(
            size_hint = (.9,.9),
            pos_hint = {'center_x': .5},
            font_size = 27,
            duration = .025)
            # (satu animate bisa terdiri beberapa element seperti size_hint, background_color dll)
            # (parameter t untuk transition, lihat di dokumentasi kivy)

        # membuat animasi ke dua
        # (bisa menggunakan &= untuk membuat animasi secara bersamaan)
        animate += Animation(
            size_hint = (1,1),
            pos_hint = {'center_x': .5},
            font_size = 30,
            duration = .05)

        # amulai animasikan
        animate.start(widget)

    def change_label_animate(self):
        self.ids.animate_stuff_label.text = 'look at that!!,\nthe button have a animation'
    
    def switch_click(self, switchObject, switchValue): # switchObject, switchValue are main parameter
        # switchValue me return False dan True
        if switchValue == True:
            self.ids.switch_label.text = 'ON :D'
            self.ids.switch_label.color = r'#F8FF00'
        else:
            self.ids.switch_label.color = (1,1,1,.5)
            self.ids.switch_label.text = 'OFF :('

class WidgetBasic(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    WidgetBasic().run()
