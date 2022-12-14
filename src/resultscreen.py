from kivy.app import App
from kivy.lang import Builder
import sys
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ListProperty, NumericProperty, StringProperty
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


# kv = Builder.load_string("""
# Screen:
#     canvas:
# 		Color:
# 			rgba:[1,1,1,1]
# 		Rectangle:
# 			pos:self.pos
# 			size:self.size
#
#     BoxLayout:
#
#         orientation: 'vertical'
#         Label:
#             id:RS
#             text:'app.result'
#             font_size:18
#             bold:False
#             color:.9,.2,.1,1
#             pos: 300,400
#             halign:'right'
#             valign:'middle'
#             shorten:True
#             shorten_from:'right'
#             markup:True
#
#
#         Button:
#             text: 'Exit'
#             on_release: app.stop()
# """)


# class Screen2(App):
#
#     def build(self):
#         return kv


if __name__ == "__main__":
    Resultscreen().run()