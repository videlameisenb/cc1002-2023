#modulo triangulo: en archivo triangulo.py

#esTriangulo: num num num -> bool
#True si x, y, z forman un triangulo
#ejs: esTriangulo(3,4,5)->True, esTriangulo(1,2,3)->False
def esTriangulo(x,y,z):
    def esNum(n): return type(n)==int or type(n)==float #f interna
    assert esNum(x) and esNum(y) and esNum(z)
    return x>0 and y>0 and z>0 and x+y>z and x+z>y and y+z>x
assert esTriangulo(3,4,5)
assert not esTriangulo(1,2,3)

#perimetro: num num num -> num
#perimetro de triangulo de lados x, y, z 
#ej: triangulo(3,4,5) -> 12
def perimetro(x,y,z):
    assert esTriangulo(x,y,z)
    return x+y+z
assert perimetro(3,4,5)==12

#area: num num num -> float
#area de triangulo de lados x, y, z
#ejs: area(3,4,5) -> 6.0, area(1,1,1)->0.4...
def area(x,y,z):
    assert esTriangulo(x,y,z)
    s=perimetro(x,y,z)/2
    import math
    return round(math.sqrt(s*(s-x)*(s-y)*(s-z)),2)
assert area(3,4,5)==6.0
#assert area(1,1,1)==0.4 Assertion error
assert abs(area(1,1,1)-0.4)<0.1


#tipo: num num num -> str
#'equilatero', 'isosceles' o 'escaleno' en caso que 
#x, y, z formen un triángulo equilátero, isósceles o escaleno
#ej: tipo(1,1,1)->'equilatero'
#ej: tipo(2,2,3)->'isosceles'
#ej: tipo(3,4,5)->'escaleno'
def tipo(x,y,z):
    assert esTriangulo(x,y,z)
    if x==y and x==z:
        return 'equilatero'
    elif x==y or x==z or y==z:
        return 'isosceles'
    else:
        return 'escaleno'
assert tipo(1,1,1)=='equilatero'
assert tipo(2,2,3)=='isosceles'
assert tipo(3,4,5)=='escaleno'
