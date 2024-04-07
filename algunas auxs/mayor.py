from AB import *
#rango: AB(int) -> int
#diferencia entre el mayor y el menor del árbol A
#(A no es un ABB)
#ej: rango(AB(1,AB(-2,None,None),AB(2,None,None)))->4
#ej: rango(AB(1,None,None))->0
def rango(A):
    assert esAB(A)
    if vacio(A): return arbolVacio
    def mayor(A):
        if (A.izq==None and A.der==None) or A==None:
            return A.valor
        if A.valor<2147483648:
            return max(mayor(A.izq),mayor(A.der),A.valor)

    def menor(A):
        if (A.izq==None and A.der==None) or A==None:
            return A.valor
        return min(menor(A.izq),menor(A.der),A.valor)
        
    return mayor(A)-menor(A)

assert rango(AB(1,AB(-2,None,None),AB(2,None,None)))== 4
assert rango(AB(1,None,None)) == 0
