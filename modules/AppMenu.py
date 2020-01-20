from modules import *

def donothing():
    print("Do nothing button")


class MainMenu(Menu):
    """Creates Main menu."""

    def __init__(self, root, *args, **kwargs):
        Menu.__init__(self, root, *args, **kwargs)


        file_menu = FileMenu(self, tearoff=0)
        self.add_cascade(label=LANG.file, menu=file_menu)

        root.config(menu = self)


class FileMenu(Menu):
    """Creates File menu."""

    def __init__(self, root, *args, **kwargs):
        Menu.__init__(self, root, *args, **kwargs)

        self.add_command(label="Open", command=donothing)
        self.add_separator()
        self.add_command(label="Exit", command=root.quit)


