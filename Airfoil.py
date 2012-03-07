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

import FreeCAD, Draft, Part

class Airfoil:
	def __init__(self, obj, Wire):
		"App two point properties" 
		obj.addProperty("App::PropertyLength","Length","Airfoil","Length").Length=Wire.BoundBox.XLength
		#obj.addProperty("App::PropertyLength","Thickness","Airfoil","Thickness").Thickness=12
		obj.Proxy = self
		self.Wire = Wire
	def onChanged(self, fp, prop):
		"Do something when a property has changed"
		if(prop != 'Length'):
			return
		FreeCAD.Console.PrintMessage("Change property: " + str(prop) + "\n")
		if(fp.Length <= 0 or fp.Length == self.Wire.BoundBox.XLength):
			return
		scalefactor = fp.Length/self.Wire.BoundBox.XLength
		mat = FreeCAD.Matrix()
		mat.scale(scalefactor,scalefactor,0)
		self.Wire = fp.Shape.Wires[0].transformGeometry(mat)
		fp.Shape = self.Wire
	def execute(self, fp):
		"Print a short message when doing a recomputation, this method is mandatory" 
		fp.Shape = Part.Wire(self.Wire)
def makeAirfoil(Wire):
	a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Airfoil")
	Airfoil(a,Wire)
	a.ViewObject.Proxy=0
	FreeCAD.ActiveDocument.recompute()
