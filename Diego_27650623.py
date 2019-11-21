#!/usr/bin/env python3
"""
Proyecto Polinomio de Lagrange.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""

def polinomio_lagrange(X, Y):
    """
    Implementa y retorna el Polinomio de Lagrange para las listas X e Y.

    Parámetros:
    X: lista de valores de la variable independiente.
    Y: lista de valores de la variable dependiente.
    """

    if len(X) != len(Y): raise ValueError("Dimensiones diferentes en X e Y.")

    # Ordena el par (x, y) en forma ascendente por x.
    pares = list(zip(X, Y))
    pares.sort(key = lambda x: x[0])
    X, Y  = zip(*pares)

    def polinomio(x):
        for i in range (len(X)):
            yi= Y[i]
            for k in range (len(X)):
                if (k!=i):
                    yi=yi*((x-X[k])/(X[i]-X[k]))
            p=yi if i== 0 else p+yi                
        return p           
    return polinomio


if __name__ == '__main__':
    # Pruebe aquí su Polinomio de Lagrange ... probado con el ejemplo dado en clase
    x=-1 
    X=[2,1,-1]
    Y=[3,-2,1]

    pl=polinomio_lagrange(X,Y)
        
    print("\n"+"POLINOMIO DE LAGRANGE:"+"\n")
    print("p("+str(x)+")= "+str(pl(x)))
    print("p("+str(x+2)+")= "+str(pl(x+2))) 
    print("p("+str(x+3)+")= "+str(pl(x+3))) 
    
    pass