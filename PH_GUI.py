
import time
import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.event import EventDispatcher
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.image import Image 
#import serial

#++ser=serial.Serial('/dev/ttyUSB0')
class MainScreen(Screen):
    def Switch(self):
        self.parent.current="CPR"
    '''def Check(self, *args):
        R=str(ser.readline())
        R=str(R[0:R.find('\\')])
        T=R[0:R.find('|')]+' F'
        B=R[-1:R.find('|'):-1]+' BPM'
        (self.ids["Temperature"].text)=T
        (self.ids["BPM"]).text=B
    def on_pre_enter(self):
        Clock.schedule_interval(self.Check,1/10.)'''


class CPRScreen(Screen):
    def Switch(self):
        self.parent.current="Main"

class Manage(ScreenManager):
    pass

present=Builder.load_file("PH_GUI.kv")

class PH_GUI(App):
    def build(self):
        return present

if __name__=="__main__":
    PH_GUI().run()

