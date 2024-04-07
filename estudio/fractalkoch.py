from turtle import *
resetscreen()
#fractalKoch: int int ->
#dibujar fractal de Koch de orden n
#ej: fractalKoch(2,300)
def fractalKoch(n,L):
    assert type(n)==int and n>=1
    assert type(L)==int and L>=6

    #dibuja lado de fractal de Koch de orden n
    def lado(n,L):
        if n==1 or L<6:
            #dibuja 1 linea
            forward(L)
        else:
            #dibuja 4 lados: __/\__
            lado(n-1,L/3); left(60)
            lado(n-1,L/3); right(120)
            lado(n-1,L/3); left(60)
            lado(n-1,L/3)
    #dibuja triangulo equilatero como base
    lado(n,L); right(120)
    lado(n,L); right(120)
    lado(n,L); right(120)

fractalKoch(4,300)
