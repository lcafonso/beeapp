""" BeeApp Module """
#pylint: disable=unused-wildcard-import
#pylint: disable=wildcard-import
#pylint: disable=too-many-ancestors
from modules import *

class ToolBar:
    """

    """
    def __init__(self, root, *args, **kwargs):
        """
        ToolBar
        :param root:
        :param args:
        :param kwargs:
        """
        self.master = root
        # creating a toolbar  ==========================================================
        self.toolbar = Frame(self.master, bg="#CCC", height=60)

        # -----------------------------------------------------------------------------
        IconButton(self.toolbar, "exit.png", ICON32, LEFT, self.finaliza_software)
        IconButton(self.toolbar, "open-folder.png", ICON32, LEFT, self.openPath)
        IconButton(self.toolbar, "information.png", ICON32, LEFT, lambda: AboutWindow(Toplevel(), PATHRESOURCE+'splash.png'))
        IconButton(self.toolbar, "help.png", ICON32, LEFT, lambda: AboutWindow(Toplevel(), PATHRESOURCE+'bg.jpg'))

        self.toolbar.pack(side=TOP, fill=X)

    def finaliza_software(self):
        """
        finaliza_software
        :return:
        """
        self.master.quit()

    def openPath(self):
        """
        openPath
        :return:
        """
        aux = AppCommons._PathToOpen
        tmpdir = filedialog.askdirectory(initialdir=aux, title='Please select a directory')
        if tmpdir == '':
            AppCommons._PathToOpen = aux
            pass
        else:
            AppCommons._PathToOpen = tmpdir

        try:
            AppCommons._windowsLeft.destroy()
            AppCommons._windowsLeft = modules.FilesTree(AppCommons._frameLeft)
        except Exception as e:
            pass



    def mnu_about(self):
        """
        mnu_about
        :return:
        """
        return 0



class MainMenu(Menu):
    """Creates Main menu."""

    def __init__(self, root, *args, **kwargs):
        Menu.__init__(self, root, *args, **kwargs)


        file_menu = FileMenu(self, tearoff=0)
        self.add_cascade(label=LANG.file, menu=file_menu)

        root.config(menu=self)


class FileMenu(Menu):
    """Creates File menu."""

    def __init__(self, root, *args, **kwargs):
        Menu.__init__(self, root, *args, **kwargs)

        self.add_command(label=LANG.open, command=donothing)
        self.add_separator()
        self.add_command(label=LANG.exit, command=root.quit)


#pylint: disable=useless-object-inheritance
class BeeApp(object):
    """BeeApp"""
    def __init__(self, **kw): #pylint: disable=unused-argument
        """
        BeeApp
        :param kw:
        """

        self.root = Tk()
        #dpi_value = self.root.winfo_fpixels('1i')
        dpi_value = 200
        self.root.tk.call('tk', 'scaling', '-displayof', '.', dpi_value / 72.0)

        #Dimensionando a janela principal
        _x = int((self.root.winfo_screenwidth() - WIDTH) / 2)
        _y = int((self.root.winfo_screenheight() - HEIGHT) / 2)

        #Main window
        self.root.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, _x, _y))
        self.root.title(TITLE)
        self.root.resizable(False, False)

        # messagebox
        self.root.option_add('*Dialog.msg.font', 'Helvetica 12')
        self.root.option_add('*Dialog.msg.width', 30)
        self.root.option_add("*Dialog.msg.wrapLength", "5i")

        #Workplace
        MainMenu(self.root)  #menu
        ToolBar(self.root)   #toolbat

        fm = FrameMain(self.root) #worlplace
        fb = FrameBottom(self.root) #footer

        # Workplace setup
        ab = ActionBar(fm, width=0, height=0)
        ai = ActionInfo(ab, width=0, height=0)
        aa = ActionInfo(ab, width=0, height=0)
        ao = ActionInfo(ab, width=0, height=0)
        ap = ActionInfo(ab, width=0, height=0)

        # must keep a global reference to these two
        img1 = get_imageToButton('rotate.png',64)
        img2 = get_imageToButton('BeeIcon.png', 64)
        img3 = get_imageToButton('wall-clock.png', 64)
        img4 = get_imageToButton('computer.png', 64)

        ab.add(ai, text=LANG.tab01, image=img1, state="normal",compound=TOP)
        ab.add(aa, text=LANG.tab02, image=img2, state="normal",compound=TOP)
        ab.add(ao, text=LANG.tab03, image=img3, state="normal",compound=TOP)
        ab.add(ap, text=LANG.tab04, image=img4, state="normal",compound=TOP)

        ai.image = img1
        aa.image = img2
        ao.image = img3
        ap.image = img4

        Workplace(ai)
        Counter_program(aa)
        #Frame_examples_program(ao)
        Frame_Time(ao)
        Frame_Settings(ap)

        AboutWindow(Toplevel(), PATHRESOURCE + 'splash.png')



    def execute(self):
        """
        execute
        :return:
        """

        self.root.mainloop()





def donothing():
    """
    donothing
    :return:
    """
    print("Do nothing button")


def main(args): #pylint: disable=unused-argument
    """
    Initial Instance
    :param args:
    :return:
    """

    app_proc = BeeApp()
    app_proc.execute()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv)) #pylint: disable=undefined-variable
