from turtle import *
resetscreen()
#cuadrado: int -> 
#dibujar cuadrado de lado L pixeles
#ej: cuadrado(200)
def cuadrado(L):
    assert type(L)==int and L>=2
    #dibuja n lados de largo L
    def lados(n,L):
        if n==0: return
        forward(L);right(90)
        lados(n-1,L)
    lados(4,L)
cuadrado(200)
