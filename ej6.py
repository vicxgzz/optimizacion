# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:45:08 2020

@author: Vic-gonz
"""
import matplotlib.pyplot as py
import sympy as sy
import numpy as ny
ev=[]
res=[]
puntos_infle=[]
x=sy.Symbol('x')
y=((x*x*x*x)/12) - ((x*x*x)/2) + (x*x) + 10
def funcion(x):
  return ((x*x*x*x)/12) - ((x*x*x)/2) + (x*x) + 10
lim = ny.linspace(-6, 6, 10)
for a in lim:
    val = {x:a}
    ev.append(funcion(a))
    if(int(sy.diff(y,x,x).evalf(subs=val))==0):
      res.append(a)
for b in res:
    val = {x: b-0.1}
    sol=sy.diff(y,x,x).evalf(subs=val)
    val = {x: b+0.1}
    sol2=sy.diff(y,x,x).evalf(subs=val)
    if(sol>0 and sol2<0) or (sol<0 and sol2>0): 
     puntos_infle.append(b)        
print(puntos_infle, "puntos infleccion: ")
print(sy.diff(y,x),"1er DERIVADA")
print(sy.diff(y,x,x),"2da DERIVADA")
py.plot(lim, ev)