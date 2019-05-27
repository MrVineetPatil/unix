from math import *
def area_cirle(r):
    return (3.142*r*r)
def area_rectangle(l,b):
    return (l*b)
def area_triangle(a,b,c):
    s=(a+b+c)/2
    return (sqrt(s*(s-a)*(s-b)*(s-b))
            )