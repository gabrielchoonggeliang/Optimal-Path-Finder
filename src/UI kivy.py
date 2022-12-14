# # # # This is a sample Python script.
# # #
# # # # Press Shift+F10 to execute it or replace it with your code.
# # # # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# # #
# # #
# # # def print_hi(name):
# # #     # Use a breakpoint in the code line below to debug your script.
# # #     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
# # #
# # #
# # # # Press the green button in the gutter to run the script.
# # # if __name__ == '__main__':
# # #     print_hi('PyCharm')
# # #
# # # # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# #
#
#
#
#
#
#
#
# # import kivy
# # # kivy.require('2.1.0') # replace with your current kivy version !
# #
# # from kivy.app import App
# # from kivy.uix.label import Label
# #
# #
# # class MyApp(App):
# #
# #     def build(self):
# #         return Label(text='Hello world')
# #
# #
# # if __name__ == '__main__':
# #     MyApp().run()
# #
#
#
#
#
#
#
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
#
#
# class LoginScreen(GridLayout):
#
#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
#         self.cols = 2
#         self.add_widget(Label(text='Your initial location'))
#         self.IL = TextInput(multiline=False)
#         self.add_widget(self.IL)
#         self.add_widget(Label(text='Your target location'))
#         self.TL = TextInput(password=True, multiline=False)
#         self.add_widget(self.TL)
#
#
# class MyApp(App):
#
#     def build(self):
#         B1 = Button(text='Proceed', font_size=16)
#         B1.bind(on_press=lambda e:print("Your choices are: "))
#         # B1.canvas.add(Color(2, 2, 2, 2,))
#         # B1.canvas.add(Rectangle(pos=[200,400], size=[200, 200]))
#         return B1
#
#
# if __name__ == '__main__':
#     MyApp().run()




class ButtonTest(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



        # creat a button
        self.button01 = Button(
            text = 'B1',
            size = [200,60],
            size_hint = [None,None],
            pos=[300,540],
            background_color=(0.08, 1, 0.65, 1),
            font_size = '30px',
            color = (1, 1, 1, 1),
            state = 'down',
        )

        self.button02 = Button(
            text='B2',
            size=[140, 80],
            size_hint=[None, None],
            pos=[330, 250],
            background_color=(0.08, 1, 0.98, 1),
            font_size='30px',
            color=(1, 1, 1, 1),
            state='down',
        )

        self.button03 = Button(
            text='B3',
            size=[200, 80],
            size_hint=[None, None],
            pos=[300, 10],
            background_color=(1, 0.3, 0.5, 0.5),
            font_size='30px',
            color=(1, 0, 1, 1),
            state='down',
        )

        self.button01.bind(on_press=self.button01_clicked)
        self.button02.bind(on_press=self.button02_clicked)
        self.button03.bind(on_press=self.button03_clicked)


        self.add_widget(self.button01)
        self.add_widget(self.button02)
        self.add_widget(self.button03)




    def button01_clicked(self, bt):

        print('Your recommended way is:  ')

    def button02_clicked(self, bt2):

        print('Your recommended way is not:  ')

    def button03_clicked(self, bt3):

        print('The total optimal ways are:  ')






class ButtonTestApp(App):
    def build(self):
        return ButtonTest()


# if __name__=='__main__':
#     ButtonTestApp().run()

class TextInputWidget(Widget):
    def  __init__(self,**kwargs):
        super().__init__(**kwargs)

    def press_button(self,arg):

        start = self.ids.TP.text
        end = self.ids.IP.text
        # main()
        print('Your Optimal way is: ', start, end)

    def btn_touch_up(self):
        print("Touch Up ")
        from subprocess import Popen, PIPE
        process = Popen(['python', 'resultscreen.py'], stdout=PIPE, stderr=PIPE)


    def release_button(self,arg):
        print('Thanks for your using. Looking forward to your next process')

    def print_result(self):
        print('hello')


class ButtonFloatLayout(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


class TextInputApp(App):
    def build(self):
        return TextInputWidget()



if __name__ == '__main__':
    TextInputApp().run()

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import StringProperty

class ButtonTest(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



        # creat a button
        self.button01 = Button(
            text = 'B1',
            size = [200,60],
            size_hint = [None,None],
            pos=[300,540],
            background_color=(0.08, 1, 0.65, 1),
            font_size = '30px',
            color = (1, 1, 1, 1),
            state = 'down',
        )

        self.button02 = Button(
            text='B2',
            size=[140, 80],
            size_hint=[None, None],
            pos=[330, 250],
            background_color=(0.08, 1, 0.98, 1),
            font_size='30px',
            color=(1, 1, 1, 1),
            state='down',
        )

        self.button03 = Button(
            text='B3',
            size=[200, 80],
            size_hint=[None, None],
            pos=[300, 10],
            background_color=(1, 0.3, 0.5, 0.5),
            font_size='30px',
            color=(1, 0, 1, 1),
            state='down',
        )

        self.button01.bind(on_press=self.button01_clicked)
        self.button02.bind(on_press=self.button02_clicked)
        self.button03.bind(on_press=self.button03_clicked)


        self.add_widget(self.button01)
        self.add_widget(self.button02)
        self.add_widget(self.button03)




    def button01_clicked(self, bt):

        print('Your recommended way is:  ')

    def button02_clicked(self, bt2):

        print('Your recommended way is not:  ')

    def button03_clicked(self, bt3):

        print('The total optimal ways are:  ')






class ButtonTestApp(App):
    def build(self):
        return ButtonTest()


# if __name__=='__main__':
#     ButtonTestApp().run()

class TextInputWidget(Widget):
    def  __init__(self,**kwargs):
        super().__init__(**kwargs)

    def press_button(self,arg):

        start = self.ids.TP.text
        end = self.ids.IP.text
        # main()
        print('Your Optimal way is: ', start, end)


    def release_button(self,arg):
        print('Thanks for your using. Looking forward to your next process')


class ButtonFloatLayout(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


class TextInputApp(App):
    def build(self):
        return TextInputWidget()



if __name__ == '__main__':
    TextInputApp().run()

