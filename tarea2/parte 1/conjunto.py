from lista import *

#esConjunto: lista -> bool
#True si lista x es un conjunto (sin valores repetidos)
#ej1: esConjunto(lista(1,lista(2,None))) -> True
#ej2: esConjunto(lista(1,lista(3,lista(3,None)))) -> False
def esConjunto(x):
    assert type(x)==lista or x==listaVacia
    if vacia(x):
        return True
    else:
        if vacia(cola(x)):
            return True
        elif cabeza(x)!=cabeza(cola(x)):
            return esConjunto(cola(x))
        else:
            return False

assert esConjunto(lista(1,lista(2,None)))
assert not esConjunto(lista(1,lista(3,lista(3,None))))
assert esConjunto(listaVacia)
assert esConjunto(lista('a',lista('b',None)))

#contiene: lista num/str -> bool
#True si conjunto x contiene el valor n
#ej1: contiene(lista(1,lista(-5,None)),-5) -> True
#ej2: contiene(lista(-13,lista(4,lista(0.4,None))),7) -> False
def contiene(x,n):
    assert esConjunto(x)
    if vacia(x):
        return False
    else:
        if cabeza(x)==n:
            return True
        elif vacia(cola(x)):
            return False
        else:
            return contiene(cola(x),n)

assert contiene(lista(1,lista(-5,None)),-5)
assert not contiene(lista(-13,lista(4,lista(0.4,None))),7)
assert not contiene(listaVacia,3)
assert contiene(lista('b',lista('a',None)),'a')

#iguales: lista lista -> bool
#True si los conjuntos x e y son iguales
#ej1: iguales(listaVacia, lista(1,None)) -> False
#ej2: iguales(lista(1,lista(2,lista(3,None))),
#     lista(1,lista(2,lista(3,None)))) -> True
def iguales(x,y):
    assert esConjunto(x) and esConjunto(y)
    if largo(x)!=largo(y):
        return False
    def iguales_aux(x,y):
        if vacia(y):
            return True
        elif contiene(x,cabeza(y)):
            return iguales_aux(x,cola(y))
        else:
            return False
    return iguales_aux(x,y)

assert iguales(lista(1,lista(2,lista(3,None))),\
               lista(3,lista(2,lista(1,None))))
assert not iguales(lista(1,None),lista(-13,lista(4,lista(1,None))))
assert not iguales(listaVacia, lista(1,None))
assert not iguales(lista(1,None), listaVacia)
assert iguales(lista('a',lista('b',None)),lista('b',lista('a',None)))

#union: lista lista -> lista
#Conjunto con la unión de los conjuntos x e y
#ej1: union(listaVacia,lista(1,None)) -> lista(1,None)
#ej2: union(lista(1,lista(2,None)),lista(3,None))
#     -> lista(1,lista(2,lista(3,None)))
def union(x,y):
    assert esConjunto(x) and esConjunto(y)
    if vacia(x):
        return y
    elif contiene(y, cabeza(x)):
        return union(cola(x),y)
    else:
        return lista(cabeza(x),union(cola(x),y))

assert iguales(union(listaVacia,lista(1,None)),lista(1,None))
assert iguales(union(lista(1,lista(2,None)),lista(3,None)),\
               lista(1,lista(2,lista(3,None))))
assert iguales(union(lista(1,None),listaVacia),lista(1,None))
assert iguales(union(lista(1,lista(2,None)),lista(2,lista(1,None))), \
        lista(1,lista(2,None)))
assert iguales(union(lista('a',lista('b',None)),lista('c',None)) ,\
               lista('a',lista('b',lista('c',None))))

#inter: lista lista -> lista
#Conjunto con la intersección de los conjuntos x e y
#ej1: inter(lista(1,lista(2,None)), lista(2,None)) -> lista(2,None)
#ej2: inter(lista(3,None),lista(2,lista(3,None))) -> lista(3,None)
def inter(x,y):
    assert esConjunto(x) and esConjunto(y)
    if vacia(x) or vacia(y): return 
    else:
        if contiene(x,cabeza(y)):
            return lista(cabeza(y),inter(x,cola(y)))
        elif contiene(y,cabeza(x)):
            return lista(cabeza(x),inter(cola(x),y))
        else:
            return inter(cola(x),cola(y))

assert iguales(inter(lista(1,None),lista(1,None)),lista(1,None))
assert iguales(inter(lista(4,lista(3,lista(2,lista(1,None)))),lista(1,None)),\
               lista(1,None))
assert iguales(inter(lista(3,None),lista(2,lista(3,None))),lista(3,None))
assert iguales(inter(lista(3,None),lista(2,lista(4,None))),listaVacia)
assert iguales(inter(lista('b',lista('a',None)),lista('a',None)) ,\
               lista('a',None))

#escribir: lista -> str
#Escribir elementos de conjunto x
#ej1: escribir(lista(1,None)) -> 1
#ej2: escribir(lista('hola',lista('chao',None))) -> 'hola' 'chao'
def escribir(x):
    assert esConjunto(x)
    if vacia(x):
        return ''
    else:
        print(cabeza(x))
        escribir(cola(x))

#ej1: escribir(lista(1,None))
# -> 1
#ej2: escribir(lista('hola',lista('chao',None)))
# -> 'hola'
# -> 'chao'
