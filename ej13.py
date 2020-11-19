# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 22:24:26 2020

@author: Vic-gonz
"""
import numpy as ny
import matplotlib.pyplot as py
import sympy as sy
x=sy.Symbol('x')
ev=[]
r1=[]
r2=[]
r3=[]
def funcion(x):
  return ((x*x*x*x)/4)-((9*(x*x))/2)
y=((x*x*x*x)/4)-((9*(x*x))/2)
lim = ny.linspace(-5, 5, 11)
for i in lim:
    val = {x:i}
    ev.append(funcion(i))
    if(int(sy.diff(y,x,).evalf(subs=val))==0):
      r1.append(i)    
for j in r1:
  r2.append(funcion(j))
for z in r1:
    values = {x:z}
    r3.append(sy.diff(y,x,x).evalf(subs=values))    
for a in range(len(r1)):
    if(r3[a]>0):
        print("cóncava hacia arriba en x=",r1[a]," y mínimo relativo :",r1[a],",",r2[a],"")
    else:
        if(r3[a]<0):
            print("cóncava hacia abajo en x=",r1[a]," y maximo relativo :",r1[a],",",r2[a],"")
        else:
           print("ninguna solucion para concavidad en x=",r1[a])
print(sy.diff(y,x), "1ra DERIVADA")
print( sy.diff(y,x,x), "2da DERIVADA")
print(r1, "valores ")           
py.plot(lim, ev)