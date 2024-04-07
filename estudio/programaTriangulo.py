from  triangulo import *
print('Tipo, área y perímetro de triángulo de lados a,b,c')
a=float(input('a?'))
b=float(input('b?'))
c=float(input('c?'))
if esTriangulo(a,b,c):
  print("tipo:", tipo(a,b,c))
  print("perímetro:", perimetro(a,b,c))
  print("área:", area(a,b,c))
else:
  print("no forman un triángulo")



