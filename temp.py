      # -*- coding: utf-8 -*- 
import math

# The functions
#TODO SyntaxTest umkehrfunktion: sinNOK
def funcfx(x): return math.sin(math.radians(x)**2) - x**(0.5) + x**3 - 12

def funcgx(x): return x**math.pi + (2**(0.5))/x - 3**x -2

def funchx(x): return ((x**2+2)/(x**3-2*x+4))-((math.e**(2*x)-x**(1/3))/(4*x-8*x**2))-4
#umkehrfunktion NOK, mit cos aufpassen
def funcix(x): return math.cos(math.radians((2*x)))+0.5*(math.cos(math.radians(x**2)))+math.pi**x-4

def functestx(x): return (math.cos(math.radians(x*2)) + 0.5*(math.cos(math.radians(x**2))) + math.pi**x -4)

# Method to calculate Difference Quotient
h = 1e-7 

def dfa(f, x, h):
    return (f(x + h) - f(x)) / h


x= 3
print(math.pi**0.2)
#correct 
print((math.cos(math.radians(2*x)) + 0.5*(math.cos(math.radians(x**2))) + math.pi**x -4))
#umkehrfunktion = -2sin(2x)-x*sin(x**2)+ln(pi)*pi**x == 34.81 with x=3 NOK
print("ix with x0= ",x, "-> funktion= ", funcix(x),  " || umkehrfunktion= ", dfa(funcix, x, h))
#correct
print(-2*(math.sin(math.radians(2*x)))-x*math.sin(math.radians(x**2))+math.log(math.pi)*math.pi**x)


"""
#print the difference Quotient
print("fx with x0= ",2.25, "-> funktion= ", funcfx(2.25),  " || umkehrfunktion= ", dfa(funcfx, 2.25, h))
print("gx with x0= ",1.875, "-> funktion= ", funcgx(1.875),  " || umkehrfunktion= ", dfa(funcgx, 1.875, h))
print("hx with x0= ",2, "-> funktion= ", funchx(2),  " || umkehrfunktion= ", dfa(funchx, 2, h))
print("ix with x0= ",2.25, "-> funktion= ", funcix(2.25),  " || umkehrfunktion= ", dfa(funcix, 2.25, h))
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
x = 2.25
print("fx with x0= ",x, "-> funktion= ", funcfx(x),  " || umkehrfunktion= ", dfa(funcfx, x, h))
x = 1.875
print("gx with x0= ",x, "-> funktion= ", funcgx(x),  " || umkehrfunktion= ", dfa(funcgx, x, h))
x = 2
print("hx with x0= ",x, "-> funktion= ", funchx(x),  " || umkehrfunktion= ", dfa(funchx, x, h))
x = 2.25
print("ix with x0= ",x, "-> funktion= ", funcix(x),  " || umkehrfunktion= ", dfa(funcix, x, h))
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
"""

#Newtonsverfahren_v1
x = 2.25
print("_____________________________FUNC f(x) __________________________________________")
#OK
for i in range(10):
    
    x = x - ((funcfx(x))/(dfa(funcfx, x, h)))
    if funcfx(x) < 0.00001:
                print('the solution is: x0=', x, ' f(x)=',funcfx(x))
                break
#TipTop
x = 2 
print("_____________________________FUNC g(x) __________________________________________")
for i in range(100):
    
    x = x - ((funcgx(x))/(dfa(funcgx, x, h)))
    if funcgx(x) < 0.00001:
            print("the solution is: x0= ",x, "func: ",funcgx(x))
            break
x = 2
print("_____________________________FUNC h(x) __________________________________________")
for i in range(100):
    
    x = x - ((funchx(x))/(dfa(funchx, x, h)))
    if funchx(x) < 0.00001:
            print("the solution is: x0= ",x, "func: ",funchx(x))
            break       
x = 2
print("_____________________________FUNC i(x) __________________________________________")
for i in range(100):
    
    x = x - ((funcix(x))/(dfa(funcix, x, h)))
    if funcix(x) < 0.00001:
            print("the solution is: x0= ",x, "func: ",funcix(x))
            break
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
#Newtonsverfahren_v2
print("Function f(x)")
x = 2.25
i = 1
while i < 100:
    
    x = x - ((funcfx(x))/(dfa(funcfx, x, h)))
    i += 1
    if funcfx(x) < 0.00001:
                print('the solution is: x0=', x, ' f(x)=',funcfx(x), 'iteration:', i)
                break
                
#TipTop
x = 2 
i = 1
print("Function g(x)")
while i < 100:
    
    x = x - ((funcgx(x))/(dfa(funcgx, x, h)))
    i += 1
    if funcgx(x) < 0.00001:
            print("the solution is: x0= ",x, "func: ",funcgx(x), "iteration= ", i)
            break
            
x = 0.65
i = 1
print("Function h(x)")
while i < 100:
    
    x = x - ((funchx(x))/(dfa(funchx, x, h)))
    i += 1
    if funchx(x) < 0.00001:
            print("the solution is: x0= ",x, "func: ",funchx(x), "i= ", i)
            break      
            
x = 1.25
i = 1
print("Function i(x)")
while i < 100:
    
    x = x - ((funcix(x))/(dfa(funcix, x, h)))
    i += 1
    if funcix(x) < 0.00001:
            print("the solution is: x0= ",x, "func: ",funcix(x), "i= ", i)
            break
x = 1.25
i = 1
print("Function test(x)")
while i < 100:
    print("the solution is: x0= ",x, "func: ",functestx(x), "i= ", i)
    x = x - (functestx(x))/(dfa(functestx, x, h))
    
    i += 1
    if functestx(x) < 0.000001:
            print("the solution is: x0= ",x, "func: ",functestx(x), "i= ", i)
            break
            
'''       
#Newtonsverfahren_draft
print("newton====================================================================")
n=100
x0=2.25
for val in range(1,n):
    x2 = x0 - funcfx(x0)/dfa(funcfx, x0, h)
    if funcfx(x2) < 0.00001:
            print('the solution is: ', x2, 'funktion= ',funcfx(x2))
            break
    x0 = x2
print("waspassiert?====================================================================")  
def newton(x0, f, dfa):
    n=100
    for val in range(1,n):
            x2 = x0 - f(x0)/dfa(f, x0, h)
            if f(x2) < 0.00001:
                    print('the solution is: ', x2, 'function= ',f(x2))
                    return x2
                    break
                    x0 = x2
"""
print("//////////////////////////////////////////////////////////////////////////////")   
print(newton(2.25, funcfx, dfa))
print("//////////////////////////////////////////////////////////////////////////////")    
"""  
print("newton g(x)====================================================================")
n=10
x0=6
for val in range(1,n):
    x2 = x0 - funcgx(x0)/dfa(funcgx, x0, h)
    if funcgx(x2) < 0.00001:
            print('the solution is: ', x2, 'funktion= ',funcgx(x2), 'iteration: ', n)
            break
    x0 = x2
    
print("newton h(x)====================================================================")
n=100
x0=2.25
for val in range(1,n):
    x2 = x0 - funchx(x0)/dfa(funchx, x0, h)
    if funcfx(x2) < 0.00001:
            print('the solution is: ', x2, 'funktion= ',funchx(x2))
            break
    x0 = x2
    
print("newton i(x)====================================================================")
n=100
x0=2.25
for val in range(1,n):
    x2 = x0 - funcix(x0)/dfa(funcix, x0, h)
    if funcfx(x2) < 0.00001:
            print('the solution is: ', x2, 'funktion= ',funcix(x2))
            break
    x0 = x2
print("+++++++++++++++++++++iteration++++++++++++++++++++++++++++++++++++++++++")
i=1
x0=2.25
while i < 100:
    x2 = x0 - funchx(x0)/dfa(funchx, x0, h)
    if funchx(x2) < 0.00001:
            print('the solution is: ', x2, 'funktion= ',funcix(x2), 'iteration=', i)
            break
    x0 = x2
    i += 1
'''  
    