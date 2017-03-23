from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.graphics import *
from kivy.uix.scrollview import ScrollView


class BasicScreen(Screen):
    def __init__(self, background_img=None, size=Window.size, **kwargs):
        super(BasicScreen, self).__init__(size=size, **kwargs)
        self.background_img = background_img
        self.background_instructions = InstructionGroup()
        self.set_up_background_image()
        Window.bind(on_resize=self.fit_to_window)

    def fit_to_window(self, window, width, height):
        self.background_instructions.clear()
        self.background_instructions.add(Rectangle(pos=self.pos, size=(width, height), source=self.background_img))

    def set_up_background_image(self):
        if self.background_img:
            self.background_instructions.add(Rectangle(pos=self.pos, size=self.size, source=self.background_img))
            self.canvas.add(self.background_instructions)


class MainScreen(BasicScreen):
    def __init__(self, background_img, **kwargs):
        super(MainScreen, self).__init__(name='MainScreen', background_img=background_img, **kwargs)
        self.main_layout = RelativeLayout(id='MainLayout', orientation='vertical', size_hint=(1, 1))
        self.main_title = Label(id='MainTitle', text='BoardGameApp', font_size=30, pos_hint={'y': 0.8}, size_hint_y=0.2)
        self.maps_button = Button(id='MapsButton', text='Show map', size_hint=(0.5, 0.18),
                                  pos_hint={'x': 0.25, 'y': 0.38},
                                  on_press=lambda a: App.get_running_app().root.switch_screen('MapScreen'))
        self.games_button = Button(id='GamesButton', text='Show games', size_hint=(0.5, 0.18),
                                   pos_hint={'x': 0.25, 'y': 0.2},
                                   on_press=lambda a: App.get_running_app().root.switch_screen('ListGamesScreen'))

        self.main_layout.add_widget(self.main_title)
        self.main_layout.add_widget(self.maps_button)
        self.main_layout.add_widget(self.games_button)
        self.add_widget(self.main_layout)


class MapScreen(BasicScreen):
    def __init__(self, background_img, **kwargs):
        super(MapScreen, self).__init__(name='MapScreen', background_img=background_img, **kwargs)
        self.main_layout = RelativeLayout(id='MapLayout', orientation='vertical', size_hint=(1, 1))
        self.main_title = Label(id='MapTitle', text='Map', font_size=30, pos_hint={'y': 0.85}, size_hint_y=0.15)
        self.back_button = Button(id='BackButton', text='Back', font_size=15, size_hint=(0.1, 0.1),
                                  on_press=lambda a: App.get_running_app().root.switch_screen('MainScreen'))
        self.show_towns = Button(id='ShowTownButton', text='Show available towns', size_hint=(0.5, 0.15),
                                 pos_hint={'x': 0.25, 'y': 0.7})

        self.dropdown = DropDown()
        self.show_towns.bind(on_release=self.dropdown.open)

        for town in range(0, towns=20):
            btn = Button(id=str(town), font_size=20, size_hint_y=None, text=str(town),
                         on_press=lambda a: App.get_running_app().root.switch_screen('MainScreen'))
            self.dropdown.add_widget(btn)

        self.add_widget(self.main_title)
        self.add_widget(self.back_button)
        self.add_widget(self.show_towns)
        self.add_widget(self.main_layout)


class ListGamesScreen(BasicScreen):
    def __init__(self, background_img, **kwargs):
        super(ListGamesScreen, self).__init__(name='ListGamesScreen', background_img=background_img, **kwargs)
        self.main_layout = RelativeLayout(id='ListGamesScreen', size_hint=(1, 1))
        self.main_title = Label(id='ListGamesTitle', text='List of board games', font_size=30, size_hint=(1, 0.1),
                                pos_hint={'y': 0.9})
        self.back_button = Button(id='BackButton', text='Back', font_size=15, size_hint=(0.1, 0.1),
                                  on_press=lambda a: App.get_running_app().root.switch_screen('MainScreen'))
        self.grid_layout = GridLayout(cols=1, size_hint=(1, None), spacing=10)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))

        for num in range(0, 100):
            btn = Button(id=str(num), size_hint_y=None, font_size=20, text='Board game\'s name' + str(num),
                         on_press=lambda a: App.get_running_app().root.switch_screen('GamesScreen',
                                                                                     game_title=str(a.text)))
            self.grid_layout.add_widget(btn)

        self.scroll = ScrollView(size_hint=(0.8, 0.6), pos_hint={'x': 0.1, 'y': 0.1})
        self.scroll.add_widget(self.grid_layout)

        self.main_layout.add_widget(self.main_title)
        self.main_layout.add_widget(self.scroll)
        self.main_layout.add_widget(self.back_button)
        self.add_widget(self.main_layout)


class GamesScreen(BasicScreen):
    def __init__(self, background_img, title, **kwargs):
        super(GamesScreen, self).__init__(name='GamesScreen', background_img=background_img, **kwargs)
        self.set_screen_info(game_title=title)

    def set_screen_info(self, game_title):
        self.main_layout = FloatLayout(id='GamesScreen', size_hint=(1, 1))
        self.main_title = Label(id='GameTitle', text=str(game_title), font_size=30, pos_hint={'y': 0.9},
                                size_hint=(1, 0.1))
        self.photo = Image(size_hint=(0.3, 0.3), pos_hint={'x': 0.1, 'y': 0.6}, source='logo.png')
        self.back_button = Button(id='BackButton', text='Back', font_size=15, size_hint=(0.1, 0.1),
                                  on_press=lambda a: App.get_running_app().root.switch_screen('ListGamesScreen'))

        self.main_layout.add_widget(self.main_title)
        self.main_layout.add_widget(self.photo)
        self.main_layout.add_widget(self.back_button)
        self.add_widget(self.main_layout)

    def refresh_screen(self, **kwargs):
        self.main_layout.clear_widgets()
        self.set_screen_info(**kwargs)
