#!/usr/bin/python

import airfoil

reload(airfoil)

myairfoil = airfoil.airfoil()

myairfoil.load('clarky.dat')

myairfoil.createSketch()
