from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from driver import *

global result
result = path

class TextInputWidget(Widget):

    def  __init__(self,**kwargs):
        super().__init__(**kwargs)

    def press_button(self,arg):

        start = self.ids.TP.text
        end = self.ids.IP.text
        print('Your Optimal way is: ', start, end)

    def btn_touch_up(self):
        result = StringProperty(path)
        from subprocess import Popen, PIPE
        process = Popen(['python', 'resultscreen.py'], stdout=PIPE, stderr=PIPE)


    def release_button(self,arg):
        print('Thanks for using our app!')


class TextInputApp(App):
    def build(self):
        return TextInputWidget()

if __name__ == '__main__':
    TextInputApp().run()


