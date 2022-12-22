from kivy.app import App
from kivy.uix.widget import Widget
import UI_kivy

final_result = UI_kivy.result


class Result(Widget):

    def  __init__(self,**kwargs):
        super().__init__(**kwargs)

    def press_button1(self,arg):

        print(final_result)

class Resultscreen(App):        #App class is inherited
    r = final_result

    def build(self):
        return Result()

if __name__ == '__main__':
    Resultscreen().run()

