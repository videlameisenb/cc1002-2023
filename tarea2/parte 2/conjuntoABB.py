from AB import *

A = AB(5, \
       AB(3, AB(2,None,None) , AB(4,None,None)), \
       AB(7, AB(6,None,None) ,None))
A_ = AB(5, \
       AB(3, AB(2,None,None) , AB(4,None,None)), \
       AB(7, AB(6,None,None) ,None))
B = AB(4, \
       AB(2,AB(1,None,None),AB(3,None,None)),\
       AB(6,AB(5,None,None),None))
C = AB(4, \
       AB(2,None,AB(3,None,None)), \
       AB(6,AB(5,None,None),None))


#esConjunto: AB -> bool
#True si AB x es un conjunto (es decir si x es un ABB)
#ej: esConjunto(AB('b',AB('a',None,None),None)) -> True
def esConjunto(x):
    assert esAB(x)
    if vacio(x):
        return True
    V=x.valor; I=x.izq; D=x.der
    if vacio(I) and vacio(D):
        return True
    def menor(A):
        return A.valor if vacio(A.izq) else menor(A.izq)
    def mayor(A):
        return A.valor if vacio(A.der) else mayor(A.der)
    if vacio(I):
        return V<menor(D) and esConjunto(D)
    if vacio(D):
        return V>mayor(I) and esConjunto(I)
    return mayor(I)<V and V<menor(D) and esConjunto(I) and esConjunto(D)
    
assert esConjunto(A)
assert esConjunto(B)
assert esConjunto(A_)
assert esConjunto(arbolVacio)
assert esConjunto(AB('b',AB('a',None,None),None))


#pertenece: n AB -> bool
#True si valor x pertenece a un conjunto y
#ej: pertenece('a',AB('b',AB('a',None,None),None)) -> True
def pertenece(x,y):
    assert esConjunto(y)
    if vacio(y):
        return False
    if x<y.valor:
        return pertenece(x,y.izq)
    if x>y.valor:
        return pertenece(x,y.der)
    return True 

assert pertenece(5,A)
assert pertenece(5,B)
assert not pertenece(2,arbolVacio)
assert pertenece('a',AB('b',AB('a',None,None),None))


#iguales: AB AB -> bool
#True si los conjuntos x e y son iguales.
#ej: iguales(AB('a',None,AB('b',None,None)),AB('b',AB('a',None,None),None)) -> True
def iguales(x,y):
    assert esConjunto(x) and esConjunto(y)
    if vacio(x) or vacio(y):
        if vacio(x) and vacio(y): return True
        else: return False
    def _iguales(x,y):
        if vacio(x):
            return True
        vx=x.valor
        if pertenece(vx,y):
            return _iguales(x.izq,y) and _iguales(x.der,y)
        else:
            return False
    return _iguales(x,y)

assert not iguales(A,B)
assert not iguales(arbolVacio,A)
assert iguales(A,A_)
assert iguales(arbolVacio,arbolVacio)
assert iguales(AB('a',None,AB('b',None,None)),AB('b',AB('a',None,None),None))
assert iguales(AB('d',AB('a',None,AB('b',None,None)),AB('e',None,None)),\
               AB('b',AB('a',None,None),AB('e',AB('d',None,None),None)))


###funcion auxiliar para ocupar en fx. inter y fx. resta###
def borrar(n,A):
        if vacio(A): return arbolVacio
        R=A.valor
        if n < R: return AB(R, borrar(n,A.izq),A.der)
        if n > R: return AB(R,A.izq,borrar(n,A.der))
        if vacio(A.izq): return A.der
        if vacio(A.der): return A.izq
        def mayor(A):
            if vacio(A.der): return A.valor
            return mayor(A.der)
        R=mayor(A.izq)
        return AB(R,borrar(R,A.izq),A.der)


#inter: AB AB -> AB
#conjunto con la intersección de los conjuntos x e y
#ej: inter(AB('b',AB('a',None,None),AB('c',None,None)), AB('a',None,None)) \
#       -> AB('a',None,AB('c',None,None))
def inter(x,y):
    assert esConjunto(x) and esConjunto(y)
    if vacio(x) or vacio(y): return
    vx=x.valor ; vy=y.valor
    if pertenece(vx,y):
        return AB(vx, inter(x.izq,y), inter(x.der,y))
    else:
       return inter(borrar(vx,x),y)
    
assert iguales(inter(A,A_), A)
assert iguales(inter(B,A), C)
assert iguales(inter(A,A),A)
assert iguales(inter(A,C), AB(5,AB(3,AB(2,None,None),AB(4,None,None)),AB(6,None,None)))
assert iguales(inter(AB('b',AB('a',None,None),AB('c',None,None)),AB('a',None,None)),\
               AB('a',None,AB('c',None,None)))
assert iguales(inter(arbolVacio,arbolVacio),arbolVacio)


#resta: AB AB -> AB
#conjunto con x - y (resta de los elementos)
#ej: resta(AB('b',None,AB('c',None,None)),AB('a',None,AB('b',None,None)))
#       -> AB('c',None,None)
def resta(x,y):
    assert esConjunto(x) and esConjunto(y)
    if vacio(x): return None
    vx=x.valor; intxy=inter(x,y)
    if not pertenece(vx, y):
        return AB(vx, resta(x.izq,y), resta(x.der,y))
    else:
        return resta(borrar(vx,x),y)

assert iguales(resta(A,A_),arbolVacio)
assert iguales(resta(A,C),AB(7,None,None))
assert iguales(resta(B,A),AB(1,None,None))
assert iguales(resta(AB('b',AB('a',None,None),AB('c',None,AB('d',None,None))),\
                     AB('c',None,None)),\
               AB('b',AB('a',None,None),AB('d',None,None)))
assert iguales(resta(arbolVacio,arbolVacio),arbolVacio)
assert iguales(resta(AB('b',None,AB('c',None,None)),AB('a',None,AB('b',None,None))),AB('c',None,None))


#escribir: AB ->
#escribir elementos de conjunto x ordenados de menor a mayor
#ej: escribir(AB('b',AB('a',None,None),None)) -> 'a' 'b'
def escribir(A):
    assert esConjunto(A)
    if vacio(A): return
    escribir(A.izq)
    print(A.valor)
    escribir(A.der)

#assert escribir(AB('b',AB('a',None,None),None))
#-> 'a'
#-> 'b'

#assert escribir(AB(1,AB(2,None,None),AB(3,None,None)))
# -> 1
# -> 2
# -> 3
