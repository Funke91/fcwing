Loft = App.ActiveDocument.addObject("Part::Feature","Wing")
af1=App.ActiveDocument.Wire
af2 = Draft.move(af1,App.Vector(0,0.5,7),True)

Loft.Shape = Part.makeLoft([af1.Shape.Wires[0],af2.Shape.Wires[0]])
