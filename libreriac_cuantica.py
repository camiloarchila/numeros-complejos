"""
Created on Tue Aug  4 16:31:12 2020

@author: Camilo
"""
import math
def suma():
    a = [1,2]
    b = [3,-4]
    i=0
    res=[(a[i] + b[i])]
    res= res+[a[i+1] + b[i+1]]
    print(res[0],"+(",res[-1],")i")
def resta():
    a = [1,2]
    b = [3,-4]
    i=0
    res=[(a[i] + b[i])]
    res= res+[a[i+1] + b[i+1]]
    print(res[0],"-(",res[-1],")i")
def producto():
    a = [1,2]
    b = [3,-4]
    res = []
    i=0
    res = res + [((a[i]*b[i])-(a[i+1]*b[i+1]))]
    res = res + [((a[i]*b[i+1])+(a[i+1]*b[i]))]
    print(res[0],"+(",res[-1],")i")
def division():
    a = [1,2]
    b = [3,-4]
    real = (((a[0]*b[0])+(a[1]*b[1])),"/",((b[0]**2)+(b[1]**2)))
    img = (((a[1]*b[0])-(a[0]*b[1])),"/",((b[0]**2)+(b[1]**2)))
    print(real,"+",img,"i")
def modulo():
    a = [3,-4]
    i = 0
    mod = ((a[i]**2)+(a[i+1]**2))**0.5
    print(mod)
def conjugado():
    a = [3,-4]
    a[-1] = a[-1]*-1
    print(a[0],"+(",a[-1],")i")
def polar_cartesiano():
    pi = math.pi
    a = [4,2]
    b= [2,pi/6]
    pol = [((a[0]**2)+(a[1]**2))**0.5]
    pol = pol + [math.atan(a[0]/a[1])]
    cart = [b[0]*math.cos(b[1])]
    cart = cart + [b[0]*math.sin(b[1])]
    print(pol[0],"e^",pol[1],"i")
    print(cart[0],"+(",cart[0],")i")
#def fase():