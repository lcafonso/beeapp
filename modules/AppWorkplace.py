"""Workplace"""
from modules import *
from modules.AppCommons import *
from modules.checkboxTreeview import CheckboxTreeview
import tkinter.ttk as ttk


class Workplace(Frame):

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=1)

        AppCommons._frameLeft = FrameLeft(self)
        AppCommons._frameRight = FrameRight(self)

        AppCommons._windowsRight = ImageProcess(AppCommons._frameRight)
        AppCommons._windowsLeft = FilesTree(AppCommons._frameLeft)




class FilesTree(Frame):

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=1)

        # Window setup
        AppCommons._fa2 = FrameLeft(self)
        AppCommons._fa2.pack_propagate(0)

        AppCommons._fa3 = FrameRight(self)
        AppCommons._fa3.pack_propagate(0)

        # Seleciona ficheiros ----------------------------------------------------------
        self.fileFrame = LabelFrame(AppCommons._fa2, text=LANG.files, font=HELV10)
        self.fileFrame.pack(fill=BOTH, padx=5, pady=5, expand=1)

        self.tree = CheckboxTreeview(self.fileFrame)
        self.tree.pack(side=TOP, fill=BOTH, padx=0, pady=0)

        # scrollbars-----------------------------------------------------------
        vsb = ttk.Scrollbar(self.fileFrame, orient="vertical", command=self.tree.yview)
        vsb.pack(side='right', fill='y')
        hsb = ttk.Scrollbar(self.fileFrame, orient="horizontal", command=self.tree.xview)
        hsb.pack(side='bottom', fill='x')
        self.tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)

        self.fileFrame.update()

        self.path = AppCommons._PathToOpen
        self.dir = self.tree.insert('', 'end', text=self.path, open=True)

        self.Subs(self.path, self.dir)

        self.tree.bind("<<TreeviewSelect>>", self.tree_click_event)

        self.show_images_select(AppCommons._fa3)

    def autoscroll(self, sbar, first, last):
        """Hide and show scrollbar as needed."""
        first, last = float(first), float(last)
        if first <= 0 and last >= 1:
            sbar.grid_remove()
        else:
            sbar.grid()
        sbar.set(first, last)

    def Subs(self, path, parent):
        """

        :param path:
        :param parent:
        :return:
        """
        alist_filter = ['jpg', 'bmp', 'png', 'gif']
        for p in os.listdir(path):
            abspath = os.path.join(path, p)
            if os.path.isdir(abspath):
                parent_element = self.tree.insert(parent, 'end', text=p, open=True)
                self.Subs(abspath, parent_element)
            elif p.endswith(tuple(alist_filter)):
                parent_element = self.tree.insert(parent, 'end', text=p, open=True, tags=[abspath])

    def tree_click_event(self, event):
        """Checks if has changed"""
        self.show_images_select(AppCommons._fa3)


    def show_images_select(self, master):
        """

        :param master:
        :return:
        """
        try:
            self.labelImages.destroy()
        except (NameError, AttributeError):
            pass

        self.parent = master
        AppCommons._ImagenSelected = []
        for item in self.tree.get_checked():
            item_text2, item_text3 = self.tree.item(item, "tags")
            AppCommons._ImagenSelected.append(item_text2)

        self.labelImages = LabelFrame(self.parent, text=LANG.imgselect , font=HELV10)

        canvas = Canvas(self.labelImages, borderwidth=0, background="#ffffff")
        frame = Frame(canvas, background="#ffddff")
        vsb = Scrollbar(self.labelImages, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)

        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((2, 2), window=frame, anchor="nw")

        frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

        self.pict = []  # {}
        for index, fich in enumerate(AppCommons._ImagenSelected, start=0):
            masterImg = Image.open(fich).convert('RGBA')
            masterImg.thumbnail((350, 350))
            thumbnail = masterImg.copy()

            original = ImageTk.PhotoImage(thumbnail)

            self.pict.append(None)

            self.pict[index] = Button(frame, image=original, background='white', height=150, width=440,
                                      command=lambda c=index: self.iPressButton(c))
            self.pict[index].image = original
            self.pict[index].pack()

        self.labelImages.pack(side=TOP, fill=BOTH, padx=5, pady=5, expand='yes')

        self.parent.pack()

        def onFrameConfigure(canvas):
            '''Reset the scroll region to encompass the inner frame'''
            canvas.configure(scrollregion=canvas.bbox("all"))

    def iPressButton(self, idx):
        """

        :param idx:
        :return:
        """
        self.fich = AppCommons._ImagenSelected[idx]

        try:
            AppCommons._window.destroy()
        except Exception as e:
            pass

        AppCommons._window = ImageView(AppCommons._windowRight)
        AppCommons._window.load_image(self.fich)
        AppCommons._window.pack(fill=BOTH, expand=1, padx=5, pady=5)




class ImageProcess(Frame):
    """Imagem processing"""
    def __init__(self, *args, **kwargs):
        """
        ImageProcess
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=1)

        # view frame
        AppCommons._fa = FrameAction(self)
        AppCommons._fa.pack_propagate(0)


        self.showFrame = LabelFrame(AppCommons._fa, text=LANG.toView, font=HELV10)
        self.showFrame.pack(fill=BOTH, expand=1, padx=5, pady=5)

        AppCommons._windowRight = self.showFrame

        # option frame
        AppCommons._fc = FrameChat(self)
        AppCommons._fc.pack_propagate(0)

        self.configFrame = LabelFrame(AppCommons._fc, text=LANG.toSetup, font=HELV10)
        self.configFrame.pack(fill=BOTH, padx=5, pady=5)

        # frame setup
        self.configFrame.columnconfigure(0, weight=1)
        self.configFrame.columnconfigure(1, pad=1)
        self.configFrame.rowconfigure(0, weight=1)
        self.configFrame.rowconfigure(1, pad=1)
        self.configFrame.rowconfigure(2, pad=1)
        self.configFrame.rowconfigure(3, pad=1)
        self.configFrame.rowconfigure(4, pad=1)
        self.configFrame.rowconfigure(5, pad=1)
        self.configFrame.rowconfigure(6, pad=1)

        style = ttk.Style(self)
        style.configure("TButton", font=HELV08)

        # Open Folder
        folder_path = StringVar()
        self.lbl1 = Entry(self.configFrame, textvariable=folder_path,font=HELV08)
        folder_path.set(AppCommons._PathToSave)
        self.lbl1.config(state=DISABLED)
        self.lbl1.grid(row=6, column=0, sticky="nsew", padx=5, pady=5)


        # Button open folder
        im = AppCommons.get_imageToButton('open-folder.png', 24)
        self.btnOpen = ttk.Button(self.configFrame,
                                  text=LANG.saveas,
                                  style="TButton",
                                  image=im,
                                  compound="left",
                                  command=self.savePath)
        self.btnOpen.image = im
        self.btnOpen.state(["disabled"])
        self.btnOpen.grid(column=1, row=6, sticky="nsew", padx=5, pady=5)

        # Button Process
        im = AppCommons.get_imageToButton('cogwheels.png', 24)
        self.btnProcess = ttk.Button(self.configFrame,
                                     text=LANG.process,
                                     style="TButton",
                                     image=im,
                                     compound="left",
                                     command=lambda: self.callResp(self.showFrame))
        self.btnProcess.image = im
        self.btnProcess.state(["disabled"])
        self.btnProcess.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)


        #CheckButtons
        self.CheckVar1 = BooleanVar()
        self.CheckVar2 = BooleanVar()
        self.CheckVar3 = BooleanVar()

        Checkbutton(self.configFrame,
                    text=LANG.autoRotation,
                    font=HELV08,
                    variable=self.CheckVar1,
                    onvalue = True, offvalue = False,
                    command = lambda: self.disable_enable_to_process(self.btnProcess)).grid(column=0, row=3, sticky=W)
        # Checkbutton(self.configFrame,
        #             text=LANG.aceptRotation,
        #             font=HELV08,
        #             variable=self.CheckVar2).grid(column=0, row=4, sticky=W)
        Checkbutton(self.configFrame,
                    text=LANG.saveResult,
                    font=HELV08,
                    variable=self.CheckVar3,
                    onvalue=True, offvalue=False,
                    command=lambda : self.disable_enable_to_save(self.btnOpen,self.lbl1)).grid(column=0, row=4, sticky=W)

        AppCommons._AutoRotation = self.CheckVar1
        AppCommons._AceptRotation = self.CheckVar2
        AppCommons._SaveResult = self.CheckVar3

    def disable_enable_to_process(self, parent):
        """

        :param parent:
        :return:
        """
        if self.CheckVar1.get() == False:
            # self.disable_button(self.btnOpen)
            parent.state(["disabled"])
        else:
            # self.enable_button(self.btnOpen)
            parent.state(["!disabled"])

    def disable_enable_to_save(self, parent1, parent2):
        """

        :param parent1:
        :param parent2:
        :return:
        """
        if self.CheckVar3.get()==False:
            #self.disable_button(self.btnOpen)
            parent1.state(["disabled"])
            parent2.config(state=DISABLED)
        else:
            #self.enable_button(self.btnOpen)
            parent1.state(["!disabled"])
            parent2.config(state=NORMAL)


    def savePath(self):
        """

        :return:
        """
        aux = AppCommons._PathToSave
        tmpdir = filedialog.askdirectory(initialdir=aux, title=LANG.selectFolder)
        if tmpdir == '':
            AppCommons._PathToSave = aux
            pass
        else:
            AppCommons._PathToSave = tmpdir

        check_folder = os.path.isdir(AppCommons._PathToSave)
        if not check_folder:
            resp = MessageBox.askyesno(LANG.folderNot, LANG.askToCreateFolder)
            if resp==True:
                os.makedirs(AppCommons._PathToSave)
                print("created folder : ", AppCommons._PathToSave)
            else:
                print("Escolha outra : ", AppCommons._PathToSave)
                pass
        else:
            resp = MessageBox.askyesno(LANG.folderExist, LANG.askToSaveFolder)
            if resp==True:
                print( "Salvar em: " +  AppCommons._PathToSave)
            else:
                print("Escolha outra : ", AppCommons._PathToSave)
                pass




    def callResp(self, master):
        """

        :param master:
        :return:
        """
        self.config(cursor="watch")

        try:
            AppCommons._window.destroy()
        except Exception as e:
            pass

        AppCommons._window = AppCommons._windowRight
        AppCommons._window.pack(fill=BOTH, expand=1, padx=5, pady=5)

        basewidth = AppCommons.PWIDTH
        baseheight = AppCommons.PHEIGHT

        currentValue = 0
        nImages = len(AppCommons._ImagenSelected)



        # option frame
        fBar = Frame(AppCommons._windowRight, width = 410, height = 150, highlightbackground="black", highlightcolor="black", highlightthickness=1, bd=0)
        fBar.pack(side = BOTTOM )
        var = StringVar()
        label = Label(fBar, textvariable=var, relief=RAISED, font=HELV08, borderwidth=0)
        self.progressbar = ttk.Progressbar(fBar, orient="horizontal", length=400, mode="determinate")
        self.progressbar["value"] = currentValue
        self.progressbar["maximum"] = nImages
        self.progressbar.pack(side=TOP)

        var.set(LANG.processImage)
        label.pack()
        if nImages == 0:
            resp = MessageBox.showerror(LANG.warning, LANG.noImageto)
        else:
            if AppCommons._AutoRotation.get() == True:
                for item in AppCommons._ImagenSelected:
                    a = subprocess.check_output(["python", "model/image_orientation.py", "-i", item])
                    currentValue=currentValue+1
                    choice = int(a.decode())
                    self.rotate_image(master, item, choice)
                    self.progressbar.after(0, self.progress(currentValue))
                    self.progressbar.update()


            else:
                print("The checkbutton 1 value when selected is {}".format(AppCommons._AutoRotation.get()))
                print("The checkbutton 2 value when selected is {}".format(AppCommons._AceptRotation.get()))
                print("The checkbutton 3 value when selected is {}".format(AppCommons._SaveResult.get()))


        fBar.destroy()

        self.config(cursor="")

        self.canvas = Canvas(master, borderwidth=0, background="#ffffff")
        self.frame = Frame(self.canvas, background="#ffffff")
        self.vsb = Scrollbar(master, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        for row in range(len(AppCommons._ImagenAux)):
            Label(self.frame,
                  image=AppCommons._ImagenAux[row],
                  width=basewidth,
                  height=baseheight,
                  borderwidth="1",
                  relief="solid").grid(row=row, column=0)


    def progress(self, currentValue):
        self.progressbar["value"] = currentValue

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    def rotate_image(self, master, filename, choice):
        """

        :param master:
        :param filename:
        :param choice:
        :return:
        """
        basewidth = AppCommons.PWIDTH
        baseheight = AppCommons.PHEIGHT

        # image
        image = Image.open(filename).convert('RGB')
        old_size = image.size

        ratio = float(basewidth) / max(old_size)
        new_size = tuple([int(x * ratio) for x in old_size])

        if choice == 0:
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
        elif choice == 1:
            image = image.transpose(Image.FLIP_LEFT_RIGHT)
        elif choice == 2:
            image = image.transpose(Image.FLIP_TOP_BOTTOM)


        image = image.resize(new_size, Image.BILINEAR)

        if self.CheckVar3.get() == True:
            newName = filename.rsplit('/',1)[1]
            image.save(AppCommons._PathToSave+'/'+newName)

        image = ImageTk.PhotoImage(image)

        AppCommons._ImagenAux.append(image)


class ImageView(Frame):
    """ """
    def __init__(self, *args, **kwargs):
        """
        ImageView
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        try:
            self.frame.destroy()
        except Exception as e:
            pass

        self.frame = Frame

    def load_image(self, filename):
        self.utilbar = Frame(self, bg="#CCC", height=60)
        self.utilbar.pack(side=LEFT)

        basewidth = AppCommons.PWIDTH
        baseheight = AppCommons.PHEIGHT

        # image
        self.fig_image = Image.open(filename).convert('RGBA')
        old_size = self.fig_image.size

        self.teste = self.fig_image

        ratio = float(basewidth) / max(old_size)
        new_size = tuple([int(x * ratio) for x in old_size])

        self.fig_image = self.fig_image.resize(new_size, Image.BILINEAR)
        self.fig_image = ImageTk.PhotoImage(self.fig_image)

        icx = 50
        icy = 50

        # create the canvas, size in pixels
        self.canvas = Canvas(self, width=basewidth, height=baseheight, highlightthickness=0)
        #AppCommons._canvas = self.canvas
        self.image_on_canvas = self.canvas.create_image(int(basewidth/2),int(baseheight/2), anchor=CENTER, image=self.fig_image)
        #AppCommons._image_on_canvas = self.image_on_canvas

        #Icons Buttons
        AppCommons.iconButton(self.utilbar, "photo-of-a-landscape.png", icx, icy, lambda: ZoomWindow(Toplevel(), filename))
        AppCommons.iconButton(self.utilbar, "90cw.png", icx, icy, lambda: self.mnu_image(self.canvas, self.image_on_canvas,filename, 90))
        AppCommons.iconButton(self.utilbar, "90ccw.png", icx, icy,lambda: self.mnu_image(self.canvas, self.image_on_canvas,filename, -90))
        AppCommons.iconButton(self.utilbar, "fliph.png", icx, icy, lambda: self.mnu_image(self.canvas, self.image_on_canvas,filename, 180))
        AppCommons.iconButton(self.utilbar, "flipv.png", icx, icy, lambda: self.mnu_image(self.canvas, self.image_on_canvas,filename, -180))


        # pack the canvas into a frame/form
        self.canvas.pack()

    def mnu_image(self, master, parent, filename, choice):
        """

        :param master:
        :param parent:
        :param filename:
        :param choice:
        :return:
        """
        image = Image.open(filename).convert('RGB')

        angle = choice

        if angle in (-90, 90):
            image = image.rotate(angle, expand=True)
        elif angle == -180:
            image = image.transpose(Image.FLIP_TOP_BOTTOM)
        elif angle == 180:
            image = image.transpose(Image.FLIP_LEFT_RIGHT)

        image.save(filename)

        imagetk = ImageTk.PhotoImage(image)

        master.itemconfig(parent, image=imagetk)

        master.focus_set()
        master.imagetk = imagetk



