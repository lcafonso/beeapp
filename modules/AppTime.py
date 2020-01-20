"""AppTab03"""
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from functools import partial
import time

from modules import *
from modules.AppCommons import *

from  .jdutil import *

time1 = ''

class Frame_Time(Frame):
    """Counter_program"""
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=1)

        self.window = FrameMain(self, background="black")

        self.create_widgets()

    def create_widgets(self):
        self.window['padx'] = 5
        self.window['pady'] = 5


        clock_lt = Label(self.window, font=('arial', int(230/2), 'bold'), fg='red', bg='black')
        clock_lt.pack()

        date_iso = Label(self.window, font=('arial', int(75/2), 'bold'), fg='red', bg='black')
        date_iso.pack()

        date_etc = Label(self.window, font=('arial', int(40/2), 'bold'), fg='red', bg='black')
        date_etc.pack()

        clock_utc = Label(self.window, font=('arial', int(230/2), 'bold'), fg='gray50', bg='black')
        clock_utc.pack()



        def tick():
            global time1
            time2 = time.strftime('%H:%M:%S')  # local
            time_utc = time.strftime('%H:%M:%S', time.gmtime())  # utc
            # MJD
            date_iso_txt = time.strftime('%Y-%m-%d') + "    %.5f" % mjd_now()
            # day, DOY, week
            date_etc_txt = "%s   DAY: %s  Week: %s" % (time.strftime('%A'), time.strftime('%j'), time.strftime('%W'))

            if time2 != time1:  # if time string has changed, update it
                time1 = time2
                clock_lt.config(text=time2)
                clock_utc.config(text=time_utc)
                date_iso.config(text=date_iso_txt)
                date_etc.config(text=date_etc_txt)
            # calls itself every 200 milliseconds
            # to update the time display as needed
            # could use &gt;200 ms, but display gets jerky
            clock_lt.after(20, tick)

        tick()

