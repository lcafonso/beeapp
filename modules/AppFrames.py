"""AppFrames"""
from modules import *
from modules.AppCommons import *

class FrameMain(Frame):
    """FrameMain"""
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=1)

class FrameRight(Frame):
    """FrameRight"""
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=1, side="right")

class FrameLeft(Frame):
    """FrameLeft"""
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=1, side="left")

class FrameChat(Frame):
    """FrameChat"""
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=1, side="bottom")

class FrameBottom(Frame):
    """FrameBottom"""
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH)
        self.cb = ComboboxCommands(self, width=10, state="readonly")
        self.cl = CommandLine(self, relief="ridge", bd=2)
        self.bs = ButtonSend(self, text=LANG.send, relief="ridge")

class FrameAction(Frame):
    """FrameAction"""
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=1, side="top")

class ComboboxCommands(ttk.Combobox):
    """ComboboxCommands"""
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.pack(side="left", fill=BOTH)

class ActionBar(ttk.Notebook):
    """ActionBar"""
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.pack(expand=1, fill=BOTH)

        # style = ttk.Style()
        # style.theme_create( "MyStyle", parent="alt", settings={
        #         "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        #         "TNotebook.Tab": {"configure": {"padding": [50, 10] },}})
        #
        # style.theme_use("MyStyle")


class ActionInfo(Frame):
    """ActionInfo"""
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=1)

class CommandLine(Entry):
    """CommandLine"""
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.pack(side="left", fill=BOTH, expand=1)

class ButtonSend(Button):
    """ButtonSend"""
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.pack(side="right")
