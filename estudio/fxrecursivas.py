#factorial: int -> int
#calcula factorial de entero n >= 0
#ej: factorial(4) -> 24
#ej: factorial(0) -> 1
 
def factorial(n):
    assert type(n)==int and n>=0
    if n<=1: return 1
    return n*factorial(n-1)

assert factorial(4)==24
assert factorial(0)==1



#mas eficiente aún
def potencia(x,y):
    assert type(x)==int or type(x)==float
    assert type(y)==int 
    assert not(x==0 and y==0)
    def _potencia(x,y):
        if y==0: return 1
        p=_potencia(x,y//2)
        if y<0:
            if y%2==0:
                return p*p
            else:
                return x*p*p
        else:
            if y%2==0:
                return 1/(p*p)
            else:
                return 1/(x*p*p)
    return _potencia(x,y)




#mcd: int int -> int
#máximo común divisor entre x e y positivos
#ej: mcd(18,24)->6, mcd(4,9)->1, mcd(7,7)->7
def mcd(x,y):
    assert type(x)==int and x>0
    assert type(y)==int and y>0
    if x==y:
        return x
    elif x%y==0:
        return y
    elif y%x==0:
        return x
    elif x>y:
        return mcd(x%y,y)
    elif x<y:
        return mcd(x,y%x)
    
assert mcd(18,24)==6
assert mcd(4,9)==1
assert mcd(7,7)==7

#suma: int int -> int
#suma de todos los números entre x e y: x + (x+1) + … + y
#ej: suma(3,5)->12, suma(3,3)->3
def suma(x,y):
    assert type(x)==int and type(y)==int
    if x==y:
        return x
    else:
        return suma(x,y-1)+y


#cuentaRegresiva: int -> 
#escribir cuenta regresiva desde n >= 0
#ej: cuentaRegresiva(5) escribe 5, 4, 3, 2, 1
def cuentaregresiva(n):
    assert type(n)==int and n>=0
    if n > 0:
        print(n)
        cuentaregresiva(n-1)
    return 















