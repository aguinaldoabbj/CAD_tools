#!/usr/bin/freecadcmd 
#Freecad must be installed
import FreeCAD
import Mesh
import Part
import sys

print(sys.argv)

stl_name = sys.argv[2]
stp_name = stl_name + '.stp'

print("Converting '%s' to '%s'" % (stl_name, stp_name))

mesh = Mesh.Mesh(stl_name)
shape = Part.Shape()
sewing_tolerance = 0.05
shape.makeShapeFromMesh(mesh.Topology, sewing_tolerance)

solid = Part.makeSolid(shape)
solid.exportStep(stp_name)
