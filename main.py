# import os
# import random
#
# from kivy.app import App
# from kivy.core.audio import SoundLoader
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.core.window import Window
# from functools import partial
#
# class SoundBoard(App):
#     def __init__(self):
#         #: The *root* widget returned by the :meth:`build` method or by the
#         #: :meth:`load_kv` method if the kv file contains a root widget.
#         self.root = None
#         self.built = False
#
#     def build(self):
#         self.appRoot = os.path.dirname(os.path.abspath(__file__))
#         self.musicFolder = os.path.dirname(os.path.abspath(__file__))+"/music"
#
#
#         self.files = os.listdir(self.musicFolder)
#         #cria o layout para o programa
#         self.masterlayout = BoxLayout(orientation="vertical")
#         self.layout = GridLayout(cols=3)
#         self.masterlayout.add_widget(self.layout)
#         self.playing = []
#         Window.borderless = False
#         # Window.size = (500,500)
#         Window.size = (400, 720)
#         counter = 0
#         for sound in self.files:
#             name, ext = os.path.splitext(sound)
#             #print("name = %s, ext= %s" %(name, ext))
#             #btn = Button(text=name)
#             # create an image a button
#             # Adding images normal.png image as button
#             # decided its position and size
#             btn = Button(text=name,
#                          color=(random.randint(0,255), random.randint(0,255), random.randint(0,255), 1),
#                          #color=(1, 1, 1, 0),
#                          #color=(128, 128, 128, 1),
#                          background_normal=os.path.join(self.appRoot, name+'.png'),
#                          background_down=name+'.png',
#                          size_hint=(.3, .3),
#                          pos_hint={"x": 0.35, "y": 0.3})
#             blacklist = ['.png', '.DS_Store']
#             if name in blacklist:
#                 counter += 1
#                 continue
#             elif ext in blacklist:
#                 counter += 1
#                 continue
#             else:
#                 print("Added %s%s (%s) as botton" %(name, ext, self.files[counter]))
#                 btn.bind(on_press=partial(self.playSound, self.files[counter]))
#                 self.layout.add_widget(btn)
#                 counter += 1
#         #botao para parar o player
#         btnStahp = Button(text="Stop", size_hint_x=1, size_hint_y = 0.3)
#         btnStahp.bind(on_press=self.stopSound)
#         self.masterlayout.add_widget(btnStahp)
#
#         # self.change_screen("home_screen", direction="backwards")
#
#         return self.masterlayout
#
#     # def change_screen(self, screen_name, direction='forward', mode = ""):
#     #     # Get the screen manager from the kv file
#     #     screen_manager = self.root.ids['screen_manager']
#     #     #print(direction, mode)
#     #     # If going backward, change the transition. Else make it the default
#     #     # Forward/backward between pages made more sense to me than left/right
#     #     if direction == 'forward':
#     #         mode = "push"
#     #         direction = 'left'
#     #     elif direction == 'backwards':
#     #         direction = 'right'
#     #         mode = 'pop'
#     #     elif direction == "None":
#     #         screen_manager.transition = NoTransition()
#     #         screen_manager.current = screen_name
#     #         return
#     #
#     #     screen_manager.transition = CardTransition(direction=direction, mode=mode)
#     #
#     #     screen_manager.current = screen_name
#
#     def playSound(self,som,instance):
#         #funcao que toca a musica/som
#         song = SoundLoader.load("music/"+som)
#         song.play()
#         self.playing.append(song)
#
#
#     def stopSound(self,instance):
#         #para todos os sons sendo tocados
#         for f in self.playing:
#             f.stop()
#
#
# SoundBoard().run()

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):
    pass
class SettingsScreen(Screen):
    pass


GUI = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        return GUI

    def change_screen(self, screen_name):
        # Get the screen manager from the kv file
        screen_manager = self.root.ids['screen_manager']
        screen_manager.transition
        screen_manager.current = screen_name
        #screen_manager = self.root.ids

MainApp().run()