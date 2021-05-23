from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.togglebutton import ToggleButtonBehavior
from kivy.graphics import Canvas,Rectangle


class Gerenciador(ScreenManager):
    pass


class Tela1(Screen):
    musica1 = SoundLoader.load('SlowDancinginTheDark.mp3')
    posicao = musica1.get_pos


    def playMusic(self, **kwargs):
        self.musica1.play()
        self.ids.pausa.background_normal = 'pause.png'


    def stopMusic(self, **kwargs):
        self.ids.pausa.state = 'normal'
        self.ids.pausa.background_normal = 'play-button.png'
        self.musica1.stop()




class Tela2(Screen):
    musica1 = SoundLoader.load('heather.mp3')
    posicao = musica1.get_pos

    def playMusic(self, **kwargs):
        self.musica1.play()
        self.ids.pausa.background_normal = 'pause.png'

    def stopMusic(self, **kwargs):
        self.ids.pausa.state = 'normal'
        self.ids.pausa.background_normal = 'play-button.png'
        self.musica1.stop()




class Test(App):
    def build(self):
        return Gerenciador()


Test().run()
