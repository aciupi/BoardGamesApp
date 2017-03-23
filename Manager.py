from kivy.uix.screenmanager import ScreenManager
from Screens import MainScreen, MapScreen, GamesScreen, ListGamesScreen

class Manager(ScreenManager):

    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)
        self.add_widget(MainScreen(background_img='abstract-mosaic-background.png'))
        self.add_widget(MapScreen(background_img='abstract-mosaic-background.png'))
        self.add_widget(ListGamesScreen(background_img='abstract-mosaic-background.png'))
        self.add_widget(GamesScreen(background_img='abstract-mosaic-background.png', title=None))

    def switch_screen(self, name, **kwargs):
        if name == 'GamesScreen':
            self.get_screen('GamesScreen').refresh_screen(**kwargs)
        self.current = name