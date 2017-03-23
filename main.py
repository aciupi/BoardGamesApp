from kivy.app import App
from kivy.core.window import Window

from Manager import Manager
from kivy import Config

Config.set('graphics', 'multisamples', '0')

class BoardGameApp(App):
    def build(self):
        Window.size = (540, 720)
        app = Manager()
        return app

if __name__ == '__main__':
    BoardGameApp().run()