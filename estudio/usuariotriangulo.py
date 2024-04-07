#programa usuario modulo triangulo
from triangulo import *

x = float(input('ingrese la medida del lado 1: '))
y = float(input('ingrese la medida del lado 2: '))
z = float(input('ingrese la medida del lado 3: '))

print('perimetro: ', perimetro_t(x,y,z))
print('area: ', area_t(x,y,z))
              
