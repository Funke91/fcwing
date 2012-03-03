#***************************************************************************
#*                                                                         *
#*  																								*
#***************************************************************************

class WingWorkbench ( Workbench ):
    """ @brief Workbench of Wing design module. Here toolbars & icons are append. """
    
    #Icon = Paths.iconsPath() + "/Ico.png"
    MenuText = str(Translator.translate("Wing design"))
    ToolTip = str(Translator.translate("Wing design"))

    def Initialize(self):
        # ToolBar
        list = ["Wing_CreateWing"]
        self.appendToolbar("Wing design",list)

Gui.addWorkbench(WingWorkbench())
