from turtle import *
resetscreen()
#fractalCuadrado: int int ->
#dibujar fractal cuadrado de orden n
#ej: fractalCuadrado(2,300)
def fractalCuadrado(n,L):
    assert type(n)==int and n>=1
    assert type(L)==int and L>=6

    #dibuja lado de fractal cuadrado de orden n
    def lado(n,L):
        if n==1 or L<6:
            #dibuja 1 linea
            forward(L)
        else:
            #dibuja 4 lados: cuadrado
            lado(n-1,L/3); left(90)
            lado(n-1,L/3); right(90)
            lado(n-1,L/3); right(90)
            lado(n-1,L/3); left(90)
            lado(n-1,L/3)
    #dibuja cuadrado como base
    lado(n,L); right(90)
    lado(n,L); right(90)
    lado(n,L); right(90)
    lado(n,L); right(90)

fractalCuadrado(2,100)
