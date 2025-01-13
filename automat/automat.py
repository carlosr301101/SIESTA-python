from random import uniform as rd
from AtomClass import Layer,outfile
"""
Esto es un ejemplo de como funciona el programa para leer la ayuda poner Layer.help()
a=Layer(0.1,0.0001,0)
a.create_layer(100)
a.show_layer()
b=Layer(0.1,0.0001,1)
b.create_layer(100)
solid=[]
for i in range(20):
    temp=Layer(0.1,0.0001,i*2)
    temp.create_layer(32)
    solid.append(temp)
graph(solid)
outfile(solid,"salida.out")

"""
#Layer.help()
#La variable {solid} es una lista de Layers y es el tipo de parametros que esperan las funciones [graph] y [outfile]

solid=[]
a=Layer(0.01,0,0.08, xcond0=0.1, xcon1=0.49, ycond0=0.1, ycon1=0.49)
a.create_layer(10,"2")
#entry_layer(a,"data.txt")
solid.append(a)
#graph(solid)
outfile(solid,file="salida.out")
#Todo esto se puede mejorar para seguir haciendolo mas dinamico y que se vea mejor la salida.