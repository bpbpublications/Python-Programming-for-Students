# Let us create a simple application with multiple screens.
# First, create a file named main.py with the following code defining classes for multiple screens:

# main.py

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import (ScreenManager, Screen, NoTransition,SlideTransition, CardTransition, SwapTransition,
FadeTransition, WipeTransition, FallOutTransition, RiseInTransition)

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

demo = Builder.load_file("multidemo.kv")
screen_manager = ScreenManager(transition=WipeTransition())

# Add the screens to the manager and then supply a name
# that is used to switch screens

screen_manager.add_widget(FirstScreen(name="FirstScreen"))
screen_manager.add_widget(SecondScreen(name="SecondScreen"))

class MultiDemoApp(App):
    def build(self):
        return screen_manager

MultiDemoApp().run()


# multidemo.kv

# The second file is the KV file named as multidemo.kv with the following code:

ScreenManagement:
    FirstScreen:
    SecondScreen:

<FirstScreen>:
    name: 'first'

    Button:
        on_release: app.root.current = 'SecondScreen'
        text: 'Click to view Screen'
        font_size: 100

<SecondScreen>:
    name: 'second'

    Button:
        on_release: app.root.current = 'FirstScreen'
        text: 'Click to navigate back'
        font_size: 100
