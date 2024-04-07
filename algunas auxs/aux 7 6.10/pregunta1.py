import estructura
from lista import *
from funcionesAbstractas import *

#temp: ciudad(str) minima(int) máxima(int)
estructura.crear(“temp”,”ciudad minima maxima”)
stgo=temp(“Santiago”,6,21) #ejemplo de variable de tipo temp
arica=temp(“Arica”,16,24)
parenas=temp(“Punta Arenas”,-3,5)

L=lista(arica,lista(santiago,lista(parenas,None)))


#tempCiudad: str lista(temp) -> temp
#temperaturas de la ciudad de nombre x en la lista L
#ej: tempCiudad(“Santiago”,L)->temp(“Santiago”,6,21)
def tempCiudad(x,L):
    assert type(x)==str and type(L)==lista
    if vacia(L): return
    c=cabeza(L)
    if c.ciudad==x:
        return c
    else:
        return tempCiudad(x,cola(x))

assert tempCiudad('Santiago',L)==temp('Santiago',6,21)
assert tempCiudad('Calama',L)==listaVacia

#mayores: lista(temp) int -> lista(temp)
#lista con las ciudades con temperaturas máximas mayores a x
#ej: mayores(L,20)->lista(arica,lista(stgo,None))
def mayores(L,x):
    assert type(x)==int and type(L)==lista
    if vacia(L): return
    else:
        return filtro(L,lambda a:a.maxima>x)

assert mayores(L,20)==lista(arica,lista(stgo,None))
assert mayores(L,240)==listaVacia
