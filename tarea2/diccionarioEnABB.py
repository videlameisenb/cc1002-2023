#reg: nombre(str) significado(str)
from estructura import crear
crear("reg","palabra significado")
R=reg("a","A") #ejemplo
#diccionario: AB(reg)
from AB import *
#ejemplo
A=AB(reg("c","C"), \
     AB(reg("a","A"),None,None), \
     AB(reg("d","D"),None,None))

#buscar: str AB -> str
#significado de palabra en D (None si no esta)
#ej: buscar("c",A)->"C“, buscar("b",A)->None
def buscar(palabra,A):
  assert type(palabra)==str 
  assert esAB(A)
  if vacio(A): return None
  R=A.valor
  if palabra < R.palabra: return buscar(palabra,A.izq)
  if palabra > R.palabra: return buscar(palabra,A.der)
  return R.significado
assert buscar("c",A)=="C"
assert buscar("b",A)==None

#agregar: str str AB -> AB
#nuevo diccionario con palabra y significado
#ej: agregar("b","B",A)-> AB(reg("c","C"), 
#   AB(reg("a","A"),None,AB(reg("b","B"),None,None)) 
#   AB(reg("d","D"),None,None))
def agregar(palabra,significado,A):
  assert type(palabra)==str and type(significado)==str 
  assert esAB(A)
  if vacio(A): return AB(reg(palabra,significado),None,None)
  #si palabra es <, agregar en árbol izquierdo
  R=A.valor
  if palabra < R.palabra:
    return AB(R,agregar(palabra,significado,A.izq),A.der)
  #si palabra es >, agregar en árbol derecho
  if palabra > R.palabra:
    return AB(R,A.izq,agregar(palabra,significado,A.der))
  #si palabra es =, devolver el mismo árbol
  return A 
assert agregar("b","B",A) == AB(reg("c","C"), \
     AB(reg("a","A"),None,AB(reg("b","B"),None,None)), \
     AB(reg("d","D"),None,None))

#cambiar: str str AB -> AB
#nuevo diccionario cambiando significado de palabra
#ej: cambiar("d","de",A)->AB(reg("c","C"),
#    AB(reg("a","A"),None,None),AB(reg("d","de"),None,None))
def cambiar(palabra,significado,A):
  assert type(palabra)==str and type(significado)==str 
  assert esAB(A)
  if vacio(A): return arbolVacio
  #si palabra es <,cambiar en árbol izquierdo
  R=A.valor
  if palabra < R.palabra:
    return AB(R, cambiar(palabra,significado,A.izq),A.der)
  #si palabra es >, cambiar en árbol derecho
  if palabra > R.palabra:
    return AB(R,A.izq,cambiar(palabra,significado,A.der))
  #si palabra es =, cambiar significado
  return AB(reg(palabra,significado),A.izq,A.der)
assert cambiar("d","de",A) == AB(reg("c","C"),\
    AB(reg("a","A"),None,None),AB(reg("d","de"),None,None))

#borrar: str AB -> AB
#nuevo diccionario sin incluir palabra
#ej: borrar("c",A)->
#    AB(reg("a","A"),None,AB(reg("d","D"),None,None))
def borrar(palabra,A):
  assert type(palabra)==str 
  assert esAB(A)
  if vacio(A): return arbolVacio
  #si palabra es <, borrar de árbol izquierdo
  R=A.valor
  if palabra < R.palabra:
    return AB(R, borrar(palabra,A.izq),A.der)
  #si palabra es >, borrar de árbol derecho
  if palabra > R.palabra:
    return AB(R,A.izq,borrar(palabra,A.der))
  #si palabra es igual, distinguir 3 casos
  #caso1: si árbol izquierdo vacío, devolver árbol derecho
  if vacio(A.izq): return A.der
  #caso2: si árbol derecho vacío, devolver árbol izquierdo
  if vacio(A.der): return A.izq
  #caso3: si árboles no son vacíos reemplazar palabra por la mayor
  # del árbol izquierdo (y borrar la mayor del árbol izquierdo)
  def mayor(A):
      if vacio(A.der): return A.valor
      return mayor(A.der)
  R=mayor(A.izq)  
  return AB(R,borrar(R.palabra,A.izq),A.der)
assert borrar("c",A)== \
       AB(reg("a","A"),None,AB(reg("d","D"),None,None))

#escribir: AB ->
#escribe palabras de A con sus significados
#ej: escribir(A) escribe a A, c C, d D
def escribir(A):
  assert esAB(A)
  if vacio(A): return
  escribir(A.izq)
  R=A.valor
  print(R.palabra, R.significado)
  escribir(A.der)
#escribir(A)
    







assert iguales(inter(A,A_), A)
assert iguales(inter(B,A), C)
assert iguales(inter(A,A),A)

assert iguales(inter(AB('a',None,AB('b',None,None)),\
                     AB('b',AB('a',None,None),None)),\
               AB('a',None,AB('b',None,None)))
assert iguales(inter(AB(4, AB(2,AB(1,None,None),AB(3,None,None)) , AB(6,AB(5,None,None),None)) ,\
                     AB(2,None,None)),\
               AB(2,None,None))

assert iguales(inter(arbolVacio,arbolVacio),arbolVacio)
assert iguales(inter(arbolVacio,AB(4,AB(2,AB(1,None,None),AB(3,None,None)),AB(6,AB(5,None,None),None))),arbolVacio)

assert iguales(inter(AB('a',None,AB('b',None,None)),\
                     AB('b',None,None)),\
               AB('b',None,None))
               

#resta(x,y) conjunto con x - y
#conjunto con x - y
#
def resta(x,y):
    assert esConjunto(x) and esConjunto(y)
    vx=x.valor; vy=y.valor
    intxy=inter(x,y)
    




AAA=AB('b',AB('a',None,None),AB('c',None,AB('d',None,None)))
aaa=AB('c',None,None)
bbb=AB('b',AB('a',None,None),AB('d',None,None))
AAC=AB('d',AB('b',AB('a',None,None),AB('c',None,None)),AB('o',AB('h',None,None),AB('z',None,None)))
ACC=AB('x','b',None)

assert iguales(resta(ACC,AAA),AB('x',None,None))


assert iguales(resta(AB('a',None,AB('b',None,None)),\
                     AB('b',None,None)),\
               AB('a',None,None))

assert iguales(resta(AAA,aaa),bbb)
assert iguales(resta(AAA,bbb),aaa)
assert not iguales(resta(AAA,aaa),arbolVacio)
assert iguales(resta(AAA,arbolVacio),AAA)
assert not iguales(resta(AB('z',AB('d',None,None),None),AB('x',None,None)),arbolVacio)




