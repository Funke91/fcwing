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

import FreeCAD, FreeCADGui, os
import Draft
import scale
import sys
from PyQt4 import QtGui,QtCore 
import Airfoil

class MakeAirfoil:
	def Activated(self):
		sel = Draft.getSelection()[0]
		Wire = 0
		try:
			Wire = sel.Shape.Wires[0]
		except Exception, e:
			return
		Airfoil.makeAirfoil(Wire)
	def IsActive(self):
		if(len(Draft.getSelection())==1):
			return True
		else:
			return False
	def GetResources(self):
		#IconPath = Paths.iconsPath() + "/Ico.png"
		MenuText = str('Create Airfoil')
		ToolTip  = str('Create an Airfoil, from any Wired Object')
		return {'MenuText': MenuText, 'ToolTip': ToolTip}
        
FreeCADGui.addCommand('Wing_MakeAirfoil', MakeAirfoil())
