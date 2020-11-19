# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 18:50:03 2020

@author: Vic-gonz
"""
import numpy as ny
import matplotlib.pyplot as py
import sympy as sy
ev=[]
res=[]
x = sy.Symbol('x')
def funcion(x):
  return x*x*x*x
y = x*x*x*x
lim = ny.linspace(-5, 5, 11)
for i in lim:
    val = {x:i}
    res.append(sy.diff(y,x,x).evalf(subs=val))
    ev.append(funcion(i))
for a in res:
    if(a==0):
        concavo="ninguna solucion sobre la concavidad"
        break
    else:
        if(a<0):
            concavo="concavidad hacia abajo"
        else:
            concavo="concavidad hacia arriba"
          
print(sy.diff(y,x), "1era DERIVADA")
print(sy.diff(y,x,x), "2da DERIVADA")
print(concavo)
py.plot(lim, ev) 

