#***************************************************************************
#*                                                                         *
#*   Copyright (c) 2012                                              		*  
#*   Jonathan Hahn <>                            									*  
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************

class WingWorkbench ( Workbench ):
    """ @brief Workbench of Wing design module. Here toolbars & icons are append. """
    import PlaneGui
    
    #Icon = Paths.iconsPath() + "/Ico.png"
    MenuText = str("Wing design")
    ToolTip = str("Wing design")

    def Initialize(self):
        list = ["Wing_CreateWing"]
        
        # ToolBar
        self.appendToolbar("Wing design",list)
        
        # Menu
        self.appendMenu("Wing design",list)

Gui.addWorkbench(WingWorkbench())
