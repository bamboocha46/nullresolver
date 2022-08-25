      # -*- coding: utf-8 -*- 
import math

# The functions

def funcfx(x): return math.sin(x)**2 - x**(0.5) + x**3 - 12
def funcgx(x): return x**math.pi + (2**(0.5))/x - 3**x -2
def funchx(x): return ((x**2+2)/(x**3-2*x+4))-((math.e**(2*x)-x**(1/3))/(4*x-8*x**2))-4
def funcix(x): return math.cos(2*x)+0.5*(math.cos(x**2))+math.pi**x-4

# Method to calculate Difference Quotient
h = 1e-7 

def dfa(f, x, h):
    return (f(x + h) - f(x)) / h
    return

#Newtonsverfahren

print("_____________________________FUNC f(x) _______________________________")
x = 2.25
i = 1
while i < 100:
    
    x = x - ((funcfx(x))/(dfa(funcfx, x, h)))
    i += 1
    if funcfx(x) < 0.00001:
                print('the solution is: x0=', x, ' f(x)=',funcfx(x), 'iteration:', i)
                break
                
x = 1.875
i = 1
print("_____________________________FUNC g(x) _______________________________")
while i < 100:
    
    x = x - ((funcgx(x))/(dfa(funcgx, x, h)))
    i += 1
    if funcgx(x) < 0.00001:
            print("the solution is: x0= ",x, "g(x): ",funcgx(x), "iteration= ", i)
            break
            
x = 0.65
i = 1
print("_____________________________FUNC h(x) _______________________________")
while i < 100:
    
    x = x - ((funchx(x))/(dfa(funchx, x, h)))
    i += 1
    if funchx(x) < 0.00001:
            print("the solution is: x0= ",x, "h(x): ",funchx(x), "iteration= ", i)
            break      
            
x = 1.25
i = 1
print("_____________________________FUNC i(x) _______________________________")
while i < 100:
    
    x = x - ((funcix(x))/(dfa(funcix, x, h)))
    i += 1
    if funcix(x) < 0.00001:
            print("the solution is: x0= ",x, "j(x): ",funcix(x), "iteration= ", i)
            break
      
def newton(x, func):
    i = 0 
    while i < 100:
            x = x - (func(x)/(dfa(func, x, h)))
            i += 1
            if func(x) < 0.00001:
                print("the solution is: x0= ", x , "function(x0): ", func(x), "iteration= ", i)
                break
x = 2                
newton(x, funcfx)
x = 1.875
newton(x, funcgx)
x = 0.65
newton(x, funchx)
x = 1.25
newton(x, funcix)
    