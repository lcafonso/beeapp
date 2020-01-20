"""AppSettings"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from configparser import ConfigParser

from modules import *
from modules.AppCommons import *

class Frame_Settings(Frame):
    """Counter_program"""
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=1)

        self.window = FrameMain(self,  background="gray50")


        self.create_widgets()


    def create_widgets(self):
        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5


        #navegation
        nav = navtabs(self.window, LEFT)

        #first frame
        self.f1 = Frame(nav())
        self.create_frame1()

        # second frame
        self.f2 = Frame(nav())
        self.create_frame2()

        # third frame
        self.f3 = Frame(nav())
        self.create_frame3()

        # third frame
        self.f4 = Frame(nav())
        self.create_frame4()

        # keeps the reference to the radiobutton (optional)
        x1 = nav.add_screen(self.f1, "Geral", 'setting.png')
        x2 = nav.add_screen(self.f2, "Language", 'languages.png')
        x3 = nav.add_screen(self.f3, "dummy", 'remote-access.png')
        x3 = nav.add_screen(self.f4, "dummy 2", 'music-and-multimedia.png')


    def create_frame1(self):
        # Create some room around all the internal frames
        self.f1['padx'] = 5
        self.f1['pady'] = 5



    def create_frame2(self):
        # Create some room around all the internal frames
        self.f2['padx'] = 5
        self.f2['pady'] = 5


        cmd_frame = ttk.LabelFrame(self.f2, text="Commands", relief=RIDGE)
        cmd_frame.pack(fill=BOTH, expand=YES)
        # this button destroys the 1st screen radiobutton
        b2 = Button(cmd_frame, text='Button 2')
        b3 = Button(cmd_frame, text='Beep 2')
        b2.pack(fill=BOTH, expand=1)
        b3.pack(fill=BOTH, expand=1)



    def create_frame3(self):
        # Create some room around all the internal frames
        self.f3['padx'] = 5
        self.f3['pady'] = 5

        c2 = Canvas(self.f3, bg="pink")

        c2.pack(fill=BOTH, expand=1)


    def create_frame4(self):
        # Create some room around all the internal frames
        self.f4['padx'] = 5
        self.f4['pady'] = 5

        c3 = Canvas(self.f4, bg="orange")

        c3.pack(fill=BOTH, expand=1)