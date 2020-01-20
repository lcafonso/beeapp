"""

"""

# make print & unicode backwards compatible
from __future__ import print_function
from __future__ import unicode_literals


from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import simpledialog as SimpleDialog
from tkinter.colorchooser import askcolor
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import font as tkFont
from tkinter import ttk as ttk
# used to check if functions have a parameter
from inspect import getfullargspec as getArgs

# import other useful classes
import os
import sys
import locale
import time  # splashscreen
import calendar  # datepicker
import datetime  # datepicker & image
import logging  # python's logger
import inspect  # for logging

from contextlib import contextmanager  # generators
from configparser import ConfigParser

try: import argparse   # argument parser
except ImportError: argparse = None

from PIL import Image, ImageTk

import subprocess

from .AppFrames import *
from .AppCommons import *
from .AppWorkplace import *
from .AppTab02 import *
from .AppTab03 import *
from .AppTime import *
from .AppSettings import *

from .checkboxTreeview import CheckboxTreeview
from .zoomWindow import ZoomWindow
from .jdutil import *

#-----------------------------------------------------------------------------
class IconButton(Frame):
    def __init__(self, frame, image, size, bside, action):
        """
        IconButton
        :param frame:
        :param image:
        :param size:
        :param bside:
        :param action:
        """
        img = Image.open(AppCommons.PATHRESOURCE+image).convert('RGBA')
        img = img.resize(size, Image.ANTIALIAS)
        eimg = ImageTk.PhotoImage(img)

        self._button = Button(frame, image=eimg, relief=FLAT, command=action)
        self._button.image = eimg
        self._button.pack(side=bside, padx=2, pady=2)


class AboutWindow(ttk.Frame):
    """ Main window class """
    def __init__(self, mainframe, path):
        """ Initialize the main Frame """
        ttk.Frame.__init__(self, master=mainframe)

        self.path = path
        self.__image = Image.open(path).convert('RGBA')
        self.imwidth, self.imheight = self.__image.size

        self.sw = self.winfo_screenwidth()
        self.sh = self.winfo_screenheight()
        self.x = int((self.sw - self.imwidth) / 2)
        self.y = int((self.sh - self.imheight) / 2)

        self.master.title(path)
        self.master.geometry('%dx%d+%d+%d' % (self.imwidth, self.imheight, self.x, self.y))
        self.master.rowconfigure(0, weight=1)  # make the CanvasImage widget expandable
        self.master.columnconfigure(0, weight=1)

        self.master.overrideredirect(True)
        self.master.wm_attributes('-type', 'splash')
        # self.master.wm_attributes('-alpha', .5)
        # Set the root window background color to a transparent color
        #self.master.config(bg='systemTransparent')


        # Create canvas and bind it with scrollbars. Public for outer classes
        self.canvas = Canvas(self.master, bg='blue', highlightthickness=0,  width=self.imwidth, height=self.imheight)
        self.canvas.grid(row=0, column=0, sticky='nswe')
        self.canvas.update()  # wait till canvas is created

        self.container = self.canvas.create_rectangle((0, 0, self.imwidth, self.imheight), width=0)

        box_image = self.canvas.coords(self.container)  # get image area
        box_canvas = (self.canvas.canvasx(0),  # get visible area of the canvas
                      self.canvas.canvasy(0),
                      self.canvas.canvasx(self.canvas.winfo_width()),
                      self.canvas.canvasy(self.canvas.winfo_height()))



        box_img_int = tuple(map(int, box_image))  # convert to integer or it will not work properly
        x1 = max(box_canvas[0] - box_image[0], 0)  # get coordinates (x1,y1,x2,y2) of the image tile
        y1 = max(box_canvas[1] - box_image[1], 0)
        x2 = min(box_canvas[2], box_image[2]) - box_image[0]
        y2 = min(box_canvas[3], box_image[3]) - box_image[1]

        image = self.__image
        imagetk = ImageTk.PhotoImage(image.resize((int(x2 - x1), int(y2 - y1)), Image.ANTIALIAS))

        self.canvas.create_image(max(box_canvas[0], box_img_int[0]),
                                 max(box_canvas[1], box_img_int[1]),
                                 anchor='nw', image=imagetk)

        self.canvas.focus_set()
        self.canvas.imagetk = imagetk

        # goButton
        btnOk = Button(self.master,
                              bg='orange',
                              fg="white",
                              text="Ok",
                              activebackground="white",
                              activeforeground="orange",
                              command=lambda : self.mnu_about(self.master),
                              bd=0)
        btnOk.place(x=x2-150, y=y2-70, anchor=NW, width=120, height=50)

        # # Button extra
        # btnTeste = Button(self.master,
        #                bg='orange',
        #                fg="white",
        #                text="Teste",
        #                activebackground="white",
        #                activeforeground="orange",
        #                command=lambda: AboutWindow(Toplevel(), './Resources/bg.jpg'),
        #                bd=0)
        # btnTeste.place(x=x2 - 310, y=y2 - 70, anchor=NW, width=120, height=50)





    def mnu_about(self, parent):
        parent.destroy()