"""
Created on Tue Aug  4 16:31:12 2020

@author: Camilo
"""
import math
def suma(a,b):
    i=0
    res=[(a[i] + b[i])]
    res= res+[a[i+1] + b[i+1]]
    return res

def resta(a,b):
    i=0
    res=[(a[i] - b[i])]
    res= res+[a[i+1] - b[i+1]]
    return res

def producto(a,b):
    res = []
    i=0
    res = res + [((a[i]*b[i])-(a[i+1]*b[i+1]))]
    res = res + [((a[i]*b[i+1])+(a[i+1]*b[i]))]
    return res

def division(a,b):
    res =[] 
    res = res + [(((a[0]*b[0])+(a[1]*b[1]))/((b[0]**2)+(b[1]**2)))]
    res = res +  [(((a[1]*b[0])-(a[0]*b[1]))/((b[0]**2)+(b[1]**2)))]
    return res

def modulo(a):
    i = 0
    mod = ((a[i]**2)+(a[i+1]**2))**0.5
    return mod

def conjugado(a):
    a[-1] = a[-1]*-1
    return a

def polar_c(polar):
    x = polar[0]*math.cos(polar[1])
    y = polar[0]*math.sin(polar[1])
    result = (round(x, 4), round(y, 4))
    return result

def carte_p(coords):
    p = math.sqrt(coords[0]**2+coords[1]**2)
    ang = fase_c(coords)
    result = (p, ang)
    return result

def fase_c(c):
    fase = math.atan(c[1]/c[0])
    if c[0] < 0 and c[1] < 0:
        result = 180 + math.degrees(fase)
    elif c[0] < 0:
        result = 180 + math.degrees(fase)
    elif c[1] < 0:
        result = 360 + math.degrees(fase)
    else:
        result = math.degrees(fase)
    return result