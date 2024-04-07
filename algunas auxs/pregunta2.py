from estructura import *
crear('reg','palabra significado')
from lista import *
D=lista(reg('a','A'),lista(reg('b','B'),lista(reg('c','C'),\
lista(reg('d','D'),None))))


#enRango: str str lista(reg) ->
#escribir palabras(y significados) de D en que x<=palabra<y
#ej: enRango('a','c',D) escribe las líneas a A y b B
def enRango(x,y,D):
    assert esLista(D)
    assert type(x)==str; assert type(y)==str
    if vacia(D):
        return
    p=cabeza(D).palabra
    s=cabeza(D).significado

    if x<=p and p<y:
        print(p,s)
        enRango(x,y,cola(D))
    else:
        enRango(x,y,cola(D))

#----------------------------------------------------------

from estructura import *
crear('reg','palabra significado')
from AB import *
D=AB(reg('c','C'),AB(reg('b','B'),AB(reg('a','A'),None,None),None),\
 AB(reg('d','D'),None,None))

#enRango: str str lista(reg) ->
#escribir palabras(y significados) de D en que x<=palabra<y
#ej: enRango('a','c',D) escribe las líneas a A y b B
def enRango(x,y,D):
    assert esAB(D)
    assert type(x)==str; assert type(y)==str
    if vacio(D): return
    v=D.valor
    p=v.palabra
    s=v.significado
    if x<=p and p<y:
        enRango(x,y,D.izq)
        print(p,s)
        enRango(x,y,D.der)
    else:
        enRango(x,y,D.izq)
        enRango(x,y,D.der)
