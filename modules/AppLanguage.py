class I18N():
    '''Internationalization'''

    def __init__(self, language):
        """
        I18N
        :param language:
        """
        if language == 'en':
            self.resourceLanguageEnglish()
        elif language == 'pt':
            self.resourceLanguagePortuguese()
        else:
            raise NotImplementedError('Unsupported language.')

    def resourceLanguageEnglish(self):
        """

        :return:
        """
        self.title = "BeeHAPPY Graphical User Interface"

        self.file = "File"
        self.files = "Files"
        self.open = "Open"
        self.new = "New"
        self.save = "Save"
        self.saveas = "Save as"
        self.exit = "Exit"
        self.quit = "Quit"
        self.help = "Help"
        self.about = "About"

        self.send = "Send"

        self.tab01 = "Rotation"
        self.tab02 = "Anothers..."
        self.tab03 = "clock"
        self.tab04 = "Preferences"

        self.WIDGET_LABEL = ' Widgets Frame '

        self.imgselect = "Selected Images"

        self.disabled = "Disabled"
        self.unChecked = "UnChecked"
        self.toggle = "Toggle"

        # Radiobutton list
        self.colors = ["Blue", "Gold", "Red"]
        self.colorsIn = ["in Blue", "in Gold", "in Red"]

        self.labelsFrame = ' Labels within a Frame '
        self.chooseNumber = "Choose a number:"
        self.label2 = "Label 2"

        self.timeZones = "All Time Zones"
        self.localZone = "Local Zone"
        self.getTime = "New York"

        self.mgrFiles = ' Manage Files '

        self.browseTo = "Browse to File..."
        self.copyTo = "Copy File To :   "

        self.toView = "View"
        self.toSetup = "Settings"
        self.process = "Process"
        self.warning = "Warning"

        self.autoRotation = "Automatic rotation"
        self.aceptRotation = "Confirm Rotation"
        self.saveResult = "Save result to disk"
        self.selectFolder = "Please select a directory"
        self.folderNot = "Folder not exist.. "
        self.askToCreateFolder = "Do you want to create?"
        self.folderExist = "Folder already exists."
        self.askToSaveFolder = "Do you want to save in this folder?"
        self.noImageto = "There are no images selected to process."
        self.processImage = "Wait for process to finish..."

    def resourceLanguagePortuguese(self):
        """
        
        :return: 
        """""
        self.title = 'BeeHAPPY Interface Grafica do Utilizador'  # with umlaut UTF-8

        self.file = "Ficheiro"
        self.files = "Ficheiros"
        self.open = "Abrir"
        self.new = "Novo"
        self.save = "Guradar"
        self.saveas = "Guardar como"
        self.exit = "Saida"
        self.quit = "Sair"
        self.help = "Ajuda"
        self.about = "Sobre"

        self.send = "Enviar"

        self.tab01 = "Rotação"
        self.tab02 = "Outros"
        self.tab03 = "Relogio"
        self.tab04 = "Preferencias"

        self.WIDGET_LABEL = ' Etiquetas Widgets '

        self.imgselect = "Imagens Selecionadas"

        self.disabled = "Desativado"
        self.unChecked = "Desmarcar"
        self.toggle = "Alternacia"

        # Radiobutton list
        self.colors = ["Azul", "Ouro", "Vermelho"]
        self.colorsIn = ["em Azul", "em Ouro", "em Vermelho"]

        self.labelsFrame = ' Etiquetas dentro de um quadro '
        self.chooseNumber = "Escolher um numero:"
        self.label2 = "Etiqueta 2"

        self.timeZones = "fuso horario"
        self.localZone = "zona local"
        self.getTime = "Lisboa"

        self.mgrFiles = ' Gerenciar ficheiros '

        self.browseTo = "Navegue por ficheiros ..."
        self.copyTo = "Copiar ficheiro para :     "

        self.toView = "Visualizar"
        self.toSetup = "Configurar"
        self.process = "Processar"
        self.warning = "Warning"

        self.autoRotation = "Rotação automatica"
        self.aceptRotation = "Confirmar rotação"
        self.saveResult = "Salvar resultado em disco"
        self.selectFolder = "Por favor selecione um diretório"
        self.folderNot = "Pasta nao exite..."
        self.askToCreateFolder = "Deseja criar?"
        self.folderExist = "Pasta ja exite..."
        self.askToSaveFolder = "Deseja salvar nesta pasta?"
        self.noImageto = "Não existem imagens selecionadas para processar."
        self.processImage = "Aguarde a finalização do processo..."










# =================================================
if __name__ == '__main__':
    language = 'en'
    inst = I18N(language)
    print(inst.title)
