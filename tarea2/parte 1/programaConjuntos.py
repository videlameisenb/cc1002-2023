from lista import *
from conjunto import *

def leerLista(pregunta='valor?',fin='.'):
  valor=input(pregunta)
  if valor==fin:
    return listaVacia
  else:
    return lista(valor, leerLista(pregunta,fin))


c1 = leerLista('conjunto1? ')
c2 = leerLista('conjunto2? ')

unionc1c2 = union(c1,c2)
interc1c2 = inter(c1,c2)

print('-------')
print('unión:')
escribir(unionc1c2)

print('-------')
print('intersección:')
escribir(interc1c2)
