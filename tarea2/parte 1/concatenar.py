from lista import *
#concatenar: lista(str) -> str
#valor1 + valor2 + ...
#ej: concatenar(lista('a',lista('b',None))) -> 'ab'
def concatenar(L):
    assert esLista(L)
    if vacia(L):
        return ''
    else:
        return str(cabeza(L)) + ' ' + concatenar(cola(L))
assert  concatenar(lista('a',lista('b',None))) == 'ab'




