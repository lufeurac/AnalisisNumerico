#Taller1
#Punto 7
 

# Metodo Biseccion. 
# Funcion 2*cos(x) + sin(x) + 0

import numpy
from matplotlib import pyplot
def func( x ):
    return 2 * numpy.cos(x) + numpy.sin(x) + 0

 
# Derivada 
# -2*sin(x) + cos(x)
def derivFunc( x ):
    return -2 * numpy.sin(x) + numpy.cos(x)

 
# Metodo de Newton
def newtonRaphson( x ):
    lista1 = []

    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:

        h = func(x)/derivFunc(x)
        print("h ->", abs(h))
        lista1.append(abs(h))

        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
        print("x ->", x)



        
    print("El valor de la raiz es : ",
                             "%.4f"% x)
   
    pyplot.plot(lista1,"g--")

    pyplot.axhline(0, color="black")
    pyplot.axvline(0, color="black")
    pyplot.xlim(-4, 4)
    pyplot.ylim(-4, 4)
    pyplot.savefig("graficaPunto7.png")
    pyplot.show() 
    


 
x0 = 2 + 1 + 0
newtonRaphson(x0)
