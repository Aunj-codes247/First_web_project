import cmath
from cmath import *

from math import *



iota = cmath.sqrt(-1)   # this is nothing but iota i.e root-1


def sin(x):
    sintheta =((cmath.exp(x*iota) - cmath.exp(-iota*(x)))/ (2*iota)).real # eular equation extension for sin theta 
    return sintheta


def cosine(x):
    costheta = ((cmath.exp(x*iota)+ cmath.exp(-iota*x))/ (2)).real
    return costheta

def tan(x):
    tantheta = ((cmath.exp(iota*x) - cmath.exp(-iota*x))/ (iota*(cmath.exp(iota*x)+ cmath.exp(-iota *x)))).real
    return tantheta

def sec(x):
    sectheta = 1/((cmath.exp(x*iota)+ cmath.exp(-iota*x))/ (2)).real

    return sectheta

def cosec(x):
    cosectheta = 1/((cmath.exp(x*iota) - cmath.exp(-iota*(x)))/ (2*iota)).real
    return cosectheta

def cot(x):
    cottheta = 1/((cmath.exp(iota*x) - cmath.exp(-iota*x))/ (iota*(cmath.exp(iota*x)+ cmath.exp(-iota *x)))).real
    return cottheta




   
    

    

    





print(cosine(pi/2))



