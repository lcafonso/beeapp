from tkinter import *
from tkinter import ttk as ttk
from .AppLanguage import I18N
from PIL import Image, ImageTk
from .zoomWindow import ZoomWindow
import os
from configparser import ConfigParser

config = ConfigParser()
config.read('beehappy.ini')

# Language - 'en' Inglish / 'pt' Portuguese
LANGUAGE = config.get('geral', 'language', fallback="en")
LANG = I18N(LANGUAGE)

# Operate System
OS = config.get('geral', 'os', fallback="linux")

# details
AUTHOR = "Luis Afonso"
COPYRIGHT = "Copyright 2019-2020, Luis Afonso"
CREDITS = [" ", " "]
LICENSE = "Apache 2.0"
VERSION = "0.012.1"
MAINTAINER = "Luis Afonso"
EMAIL  = "lafonso@ipb.pt"
STATUS = "Development"
URL = " "
TITLE = LANG.title  #"Project Bee Happy UI"

# Monitor dimension
WIDTH = 2048
HEIGHT = 1080

PWIDTH = int((WIDTH*44.740)/100)
PHEIGHT = int((HEIGHT*37.038)/100)


ICON16 = (16, 16)
ICON32 = (32, 32)
ICON64 = (64, 64)

#fonts
HELV08 = ('Helvetica', '8')
HELV10 = ('Helvetica', '10')
HELV12 = ('Helvetica', '12')

# Globals Variables
_Ratio = 0.40
_AutoRotation = False
_AceptRotation = False
_SaveResult = False
_PathToSave =  os.getcwd()
_PathToOpen = 'test'
_ImagenSelected = []
_ImagenAux = []

#Windows
_fa = ''
_fa2 = ''
_fa3 = ''
_fc = ''
_window = ''
_windowLeft = ''
_windowRight = ''
_frameRight = ''
_frameLeft = ''
_canvas = ''
_image_on_canvas = ''

PATHRESOURCE = config.get('geral', 'path_resource', fallback='./Resources/')



def get_imageToButton(image, widht):
    """
    get_imageToButton
    :param image:
    :param widht:
    :return:
    """
    img = Image.open(PATHRESOURCE+image).convert('RGBA')
    img = img.resize((widht, widht), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img

# -----------------------------------------------------------------------------
def iconButton(frame, image, widht, height, action):
    """
    iconButton
    :param frame:
    :param image:
    :param widht:
    :param height:
    :param action:
    :return:
    """
    img = Image.open(PATHRESOURCE+image).convert('RGBA')
    img = img.resize((widht, height), Image.ANTIALIAS)
    eimg = ImageTk.PhotoImage(img)

    iconbutton = Button(frame, image=eimg, relief=FLAT, command=action)
    iconbutton.image = eimg
    iconbutton.pack(side=TOP, padx=2, pady=2)

    return iconbutton


class navtabs:
    """ """
    def __init__(self, master, side=LEFT, *args, **kwargs):
        """

        :param master:
        :param side:
        :param args:
        :param kwargs:
        """


        self.active_fr = None
        self.count = 0
        self.choice = IntVar(0)

        # radiobuttons' positioning.
        if side in (TOP, BOTTOM):
            self.side = LEFT
        else:
            self.side = TOP

        # creates notebook's frames structure
        self.rb_fr = Frame(master, borderwidth=2, relief=RIDGE)
        self.rb_fr.pack(side=side, fill=BOTH)
        self.screen_fr = Frame(master, borderwidth=2, relief=RIDGE)
        self.screen_fr.pack(fill=BOTH)

    # return a master frame reference for the external frames (screens)
    def __call__(self):
        return self.screen_fr

    # add a new frame (screen) to the (bottom/left of the) notebook
    def add_screen(self, fr, title, filename):
        try:
            image = get_imageToButton(filename, 64)
        except Exception as e:
            image = None

        b = Radiobutton(self.rb_fr, text=title, image=image,
                        compound='top', indicatoron=0,
                        variable=self.choice, value=self.count,
                        command=lambda: self.display(fr))
        b.pack(fill=BOTH, side=self.side, anchor=W)
        b.image=image




        # ensures the first frame will be
        # the first selected/enabled
        if not self.active_fr:
            fr.pack(fill=BOTH, expand=1)
            self.active_fr = fr

        self.count += 1

        # returns a reference to the newly created
        # radiobutton (allowing its configuration/destruction)
        return b

    # hides the former active frame and shows
    # another one, keeping its reference
    def display(self, fr):

        self.active_fr.forget()
        fr.pack(fill=BOTH, expand=1)
        self.active_fr = fr