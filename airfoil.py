#!/usr/bin/python

import FreeCAD as App
from FreeCAD import Part,Base,Draft,Sketcher

class airfoil(object):
	def __init__(self):
		self.points_up = {}
		self.points_down = {}
	
	def load(self, filename):
		fobj = open(filename,"r")

		self.name = ""
		i = 0
		up = True

		for line in fobj:
			i = i +1
			if(i == 1):
				name = line
			else:
				line = line.strip()
		
				if len(line) == 0:
					up = False
					continue
		
				point = line[:-1].split(" ")
		
				point[0] = float(point[0])
				point[1] = float(point[1])
		
				if(up):
					self.points_up[i]=point
				else:
					self.points_down[i]=point
					
	def createSketch(self):		
		
		#Vektorliste erzeugen
		vectorlist = []
		
		#obere Punkte uebernehmen
		for pid in sorted(self.points_up.keys(), reverse=False):
			vectorlist.append(Base.Vector(self.points_up[pid][0],self.points_up[pid][1]))

			
		#untere Punkte uebernehmen	
		for pid in sorted(self.points_down.keys(), reverse=True):				
			vectorlist.append(Base.Vector(self.points_down[pid][0],self.points_down[pid][1]))
			
				
		#print vectorlist
			
		print("linien zeichnen")
		did = Draft.makeWire(vectorlist,True,None,True)
		
		Draft.move(did, Base.Vector(0,0,5), True)
				
		App.ActiveDocument.recompute()
		
		
	
