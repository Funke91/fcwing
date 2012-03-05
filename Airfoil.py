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
		self.Wire = self.Wire.transformGeometry(mat)
		fp.Shape = self.Wire
	def execute(self, fp):
		"Print a short message when doing a recomputation, this method is mandatory" 
		fp.Shape = Part.Wire(self.Wire)
def makeAirfoil(Wire):
	a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","Airfoil")
	Airfoil(a,Wire)
	a.ViewObject.Proxy=0
	FreeCAD.ActiveDocument.recompute()
