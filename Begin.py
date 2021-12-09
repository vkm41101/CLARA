import os
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
import serial


ser=serial.Serial('/dev/ttyUSB0')
class BootScreen(Screen):
    def Kill(self):
        kivy.base.stopTouchApp()
        #time.sleep(1)
        #os.system('python3 mte.py')

    def Check(self, *args):
        R=str(ser.readline())
        R=int(R[2:R.find('\\')])
        if (R>0):
            self.Kill()
            
    def on_pre_enter(self):
        Clock.schedule_interval(self.Check,1/10.)
    

class Manage(ScreenManager):
    pass

present=Builder.load_file("Begin.kv")


class Begin(App):
    def build(self):
        return present

if __name__=="__main__":
    Begin().run()
#print("ee")

