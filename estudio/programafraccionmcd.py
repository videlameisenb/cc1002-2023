from fxrecursivas import *

print('Simplificar fracción a/b')

a = int(input('a? '))
b = int(input('b? '))

mcd_ab = mcd(a,b)

a_d = int(a/mcd_ab)
b_d = int(b/mcd_ab)

print('Fracción simplificada:',a_d,'/',b_d)
