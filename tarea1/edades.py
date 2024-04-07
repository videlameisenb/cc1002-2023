#edades    int -> int
#Genera N fechas al azar entre el 1/01 y el 31/12
#de un año entre 2000 y 2023
from random import *
from fecha import *
def edades(N,hoy):
    assert N>=0 and type(N)==int
    assert esFecha(hoy)
    añox = randint(2000,2023)
    mesx = randint(1,12)
    diax = randint(1,diaMes(mesx,añox))
    fechax = (añox*10000)+(mesx*100)+diax

    if N==0:
        return 
    else:
        edades(N-1,hoy)
        escribir(fechax)
        print('edad: ', diferencia(fechax,hoy))
        print('--------------')

edades(99,20230910)  
    
