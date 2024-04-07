from conjuntoABB import *
from AB import *


def leer(pregunta='valor?',fin='.', A=arbolVacio):
    valor=str(input(pregunta))
    if valor==fin: 
        return A
    else:
        return leer(pregunta,fin,insertar(valor,A))

c1 = leer('conjunto1? ')
c2 = leer('conjunto2? ')

interc1c2 = inter(c1,c2)
restac1c2 = resta(c1,c2)

print('-------')
print('inter:')
if interc1c2==arbolVacio:
    print('Arbol Vacío')
else:
    escribir(interc1c2)

print('-------')
print('resta:')
if restac1c2==arbolVacio:
    print('Arbol Vacío')
else:
    escribir(restac1c2)
