from fxrecursivas import *
#factoriales: ->
#leer numeros enteros y escribir factoriales
#numero negativo indica fin de datos
#ej: factoriales()
def factoriales():
    n=int(input("n° entero?"))
    if n<0: return
    print("factorial:", factorial(n))
    factoriales() 
