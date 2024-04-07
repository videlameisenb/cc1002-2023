from turtle import *
resetscreen()
#poligono: int int ->
#dibujar poligono regular de N lados 
#ej: poligono(5,180)
def poligono(N,L):
  assert type(N)==int and N>=3
  assert type(L)==int and L>=2 
  def lados(n,L,angulo):
      if n==0: return
      forward(L); right(angulo)
      lados(n-1,L,angulo)
  lados(N,L,360/N)
poligono(5,180)
