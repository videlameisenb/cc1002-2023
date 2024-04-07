import estructura
from AB import *
#temp: ciudad(str) minima(int) máxima(int)
estructura.crear('temp','ciudad minima maxima')
stgo=temp('Santiago',6,21) #ejemplo de variable de tipo temp
arica=temp('Arica',16,24)
parenas=temp('Punta Arenas',-3,5)


A=AB(parenas,AB(arica,None,None),AB(stgo,None,None))

#tempCiudad: str AB(temp) -> temp
#temperaturas de la ciudad de nombre x en ABB A
#ej: tempCiudad('Santiago',A)->temp('Santiago',6,21)
def tempCiudad(x,A):
    assert esAB(A) and type(x)==str
    if vacio(A): return
    c = A.valor
    if x<c.ciudad:
        return tempCiudad(x, A.izq)
    elif x>c.ciudad:
        return tempCiudad(x, A.der)
    else:
        return temp(x, c.minima, c.maxima)

assert tempCiudad('Arica', A)==temp('Arica',16,24)
assert tempCiudad('Punta Arenas', A)==temp('Punta Arenas',-3,5)
assert tempCiudad('Santiago', A)==temp('Santiago',6,21)

    
#mayores: AB(temp) int ->
#escribir nombres de ciudades con temperaturas máximas mayores a x
#ej: mayores(A,20) escribe 'Arica' y 'Santiago'
def mayores(A,x):
    assert esAB(A) and type(x)==int
    if vacio(A): return
    c = A.valor
    if x<c.maxima:
        mayores(A.izq,x)
        print(c.ciudad)
        mayores(A.der,x)
    else:
        mayores(A.izq,x)
        mayores(A.der,x)
    
#assert mayores(A,20)==
#-> 'Arica'
#-> 'Santiago'








