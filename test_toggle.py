from kivy.app import App
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton


Builder.load_string('''

<ToggleButton>:
    on_state: app.root.on_state(self)

<MainScreen>:

    BoxLayout:

        ToggleButtons:



''')

class MainScreen(BoxLayout):

    def on_state(self, togglebutton):
        tb = togglebutton
        print(tb, tb.state, tb.text)


class ToggleButtons(StackLayout):
    lst = ["button1", "button2", "button3", "button4", "button5"]

    def __init__(self, **kwargs):
        super(ToggleButtons, self).__init__(**kwargs)
        test = True
        for n, i in enumerate(self.lst, start=1):
            print("n = %s, i = %s" % (n, i))
            if not test:
                tgbtn = ToggleButton(text = i, size_hint = (.1, .30))
            else:
                n *= .1
                tgbtn = ToggleButton(text = i, size_hint = (n, n))
            self.add_widget(tgbtn)


class MyApp(App):
     def build(self):
        return MainScreen()

MyApp().run()
