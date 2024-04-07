from AB import *
A=AB(4, \
  AB(2,AB(1,None,None),AB(3,None,None)),\
  AB(6,AB(5,None,None),None))
#enABB: any AB -> bool
#True si x está en A
#ej: enABB(3,A)->True
#ej: enABB(7,A)->False
def enABB(x,A):
    assert esAB(A)
    if vacio(A): 
        return False
    elif x<A.valor: 
      return enABB(x,A.izq)
    elif x>A.valor: 
      return enABB(x,A.der)
    else:
      return True  #x==A.valor  
assert enABB(3,A)
assert not enABB(7,A)

def enABB(x,A):
    assert esAB(A)
    if vacio(A): return False
    if x<A.valor: return enABB(x,A.izq)
    if x>A.valor: return enABB(x,A.der)
    return True  #x==A.valor  
assert enABB(3,A)
assert not enABB(7,A)

#insertar: any AB -> AB
#nuevo ABB igual a A pero con x
#ej: insertar(2,arbolVacio) -> AB(2,None,None)

#ej: insertar(1,AB(2,None,None)) ->
#    AB(2,AB(1,None,None),None) insertar a la izq

#ej: insertar(3,AB(2,None,None)) ->
#    AB(2,None,AB(3,None,None)) insertar a la der
#ej: insertar(2,AB(2,None,None))->AB(2,None,None) ya existía
def insertar(x,A):
    assert esAB(A)
    #si A esta vacío, crear nuevo árbol con x
    if vacio(A): return AB(x,None,None)
    #insertar x a la izquierda o derecha
    v=A.valor
    if x<v: return AB(v, insertar(x,A.izq), A.der)
    if x>v: return AB(v, A.izq, insertar(x,A.der))
    #si x ya existe, devolver el mismo arbol
    return A
assert insertar(2,arbolVacio)==AB(2,None,None)
assert insertar(1,AB(2,None,None))== \
                  AB(2,AB(1,None,None),None)
assert insertar(3,AB(2,None,None))== \
                  AB(2,None,AB(3,None,None))
assert insertar(2,AB(2,None,None))==AB(2,None,None)

#leer: -> AB
#ABB con valores que se leen y terminan con fin
#ej: leer()->AB('b',AB('a',None,None),AB('c',None,None))
#            si se leen b,c,a,. 
def leer(pregunta='valor?',fin='.',A=arbolVacio):
    valor=input(pregunta)
    if valor==fin: 
        return A
    else:
        return leer(pregunta,fin,insertar(valor,A))
#assert leer()==AB('b',AB('a',None,None),AB('c',None,None))
    
#escribir: AB ->
#escribe valores de A en orden ascendente
#ej: escribir(A) escribe 1 2 3 4 5 6
def escribir(A):
    assert esAB(A)
    if vacio(A): return
    escribir(A.izq)
    print(A.valor)
    escribir(A.der)
#escribir(A)

#esABB: AB -> bool
#True si x es un ABB
#ej: esABB(A)->True, esABB(AB(1,AB(2,None,None),None))->False
def esABB(x):
    assert esAB(x)
    if vacio(x): return True
    V=x.valor; I=x.izq; D=x.der
    if vacio(I) and vacio(D): return True
    def menor(A):
        return A.valor if vacio(A.izq) else menor(A.izq)
    def mayor(A): return A.valor if vacio(A.der) else mayor(A.der)
    if vacio(I): return V<menor(D) and esABB(D)
    if vacio(D): return V>mayor(I) and esABB(I)
    return mayor(I)<V and V<menor(D) and esABB(I) and esABB(D)
assert esABB(arbolVacio)
assert esABB(A)
assert not esABB(AB(1,AB(2,None,None),None))
        
