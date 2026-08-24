from cmath import *
import cmath

i = 1j


def isin(x):

    

    invsin = (-i * cmath.log(i*x + cmath.sqrt(1 - x**2))).real

    return invsin

def icos(x):

    invcos = (-i * cmath.log(x + i * cmath.sqrt(1- x**2))).real

    return invcos

def itan(x):

    invtan = ((1/2)*i * cmath.log((1-i*x)/(1+i*x)) ).real

    return invtan 


def isec(x):

    invsec = (-i * log(1/x + i * cmath.sqrt(1 - (1/x)**2))).real

    return invsec

def icosec(x):

    invcosec = (-i * cmath.log(i/x + cmath.sqrt(1 - (1/x)**2))).real

    return invcosec










    


print(isin(0.5))
print(itan(1))