# -*- coding: utf-8 -*-
from time import *
from tkinter import *

class window:
    def __init__(self):
        self.window = Tk()
        self.window.wm_title("Pomodorotimer")
        self.window.geometry("600x400")
        se

    def time_window(self):

        self.clock = Label(master = window,
                           front = ('Arial', 30),
                           fg = 'black',
                           wight = 15,
                           hight = 3)
        self.clock.pack()
        self.zeit = ''

class options:
    def requests(self, time_study, time_break, retry):
        self.time_study = time_study
        self.time_break = time_break
        self.retry = retry

class pomodoro_timer:
    def __int__(self):





________________________________________________________________________________________________________________________
class :
    def abfrageLernen(self):

        while:
            try:
                self.zeit_lernen = int(input("Wie lange bist du am lernen?"))

            except ValueError:
                continue

    def abfragePause(self):
        Schleife = 0
        while Schleife == 0:
            try:
                self.zeit_pause = int(input("Wie lange willst du pausieren?"))
                Schleife = 1
            except:
                Schleife = 0

    def abfrageWiederholung(self):
        Schleife = 0
        while Schleife == 0:
            try:
                self.wiederholung = int(input("Wie oft machst du den Spaß?"))
                Schleife = 1
            except:
                Schleife = 0

class timer:
    def __init__(self):
        self._start_timer

if __name__ == '__main__':