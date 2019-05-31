import subprocess
import math
import os
import math
import numpy as np
from time import time as epochTime
class PIntegral:
    def __init__(self,n):
        """This is constructor"""
        self.n=n
    def classLegendre(self,x):
        return legendre(self.n,x)
    def dlegendre(self,x):
        return odlegendre(self.n,x)
    def wi(self,x):
        a=self.dlegendre(x)
        b=x**2
        return (2/( (1-b) * (a**2) ))
    def first_guess(self,i):
        return math.cos(math.pi * ((i-0.25)/self.n+0.5))
    def calculate(self):
        answer=0
        for i in range(self.n):
            x=newton_raphson(self.n , self.first_guess(i))
            answer += 0.5*self.wi(x)*f(0.5*x +0.5)
        return answer

def legendre(i,x):
    if i==0 :
        return 1
    elif i==1:
        return x
    else:
        return (  ((2*i-1)/i)*float(x)*float(legendre(i-1,x)) - ((i-1)/i)*float(legendre(i-2,x)) )

def f(x):
    return (x**3/(x+1))*math.cos(x**2)

def newton_raphson(i,x0):
    x = x0 - (legendre(i,x0)/odlegendre(i,x0))
    if legendre(i,x) > 0.05 :
        return newton_raphson(i,x)
    else:
        return x

def odlegendre(i,x):
    return (i/((x**2)-1))*(x*legendre(i,x) - legendre(i-1,x))

n = input('Enter n')
P=PIntegral( eval(n))
start = epochTime()
print(f'answer is:{P.calculate()}')
end = epochTime()
print(f'took:{end-start}')
