#diaMes: int int -> int
#Cuantos días tiene el mes indicado
#ej1: diaMes(2,2023) -> 28
#ej2: diaMes(8,2023) -> 31
def diaMes(x,y):
    assert type(x)==int and type(y)==int
    assert (x>0 and x<13) and (y>=0)
    def bisiesto(y):
        return(y%4==0 and y%100!=0) or (y%400==0)

    if x<=7 and x%2==0:
        if x==2:
            if bisiesto(y)==True:
                return 29
            else:
                return 28
        else:
            return 30
    elif x<=7 and x%2!=0:
        return 31
    elif x>=8 and x%2==0:
        return 31
    elif x>=8 and x%2!=0:
        return 30

assert diaMes(1,2023)==31
assert diaMes(2,2023)==28

#esFecha: int -> bool
#Asegura que el valor indicado corresponda a una fecha con formato válido
#ej1: esFecha(20230816) -> True
#ej2: esFecha(10000140) -> False
from math import *
def esFecha(x):
    assert type(x)==int
    año = int(x//10000)                  #se extrae año
    mes = int((x%10000)//100)            #se extrae mes
    dia = int(x%100)                     #se extrae dia
    
    def bisiesto(año):
        return(año%4==0 and año%100!=0) or (año%400==0)
    
    if año<0:                           #año mayor a 0
        return False
    elif mes<1 or mes>12:               #mes entre 1 y 12
        return False
    elif dia<1 or dia>31:               #dia entre 1 y 31
        return False
    elif mes==2 and dia==29:            #si mes=2 y dia=29
        if bisiesto(año)==True:         #verificar si es año bisiesto
            return True 
        else:
            return False
    else:
        return True
        
assert esFecha(20200229)==True
assert esFecha(10000140)==False

#diferencia: int int -> int
#Entrega la diferencia de años entre 2 fechas indicadas
#ej1: diferencia(20230820,19940114) -> 29
#ej2: diferencia(20031128,20230821) -> 19
def diferencia(x,y):
    assert esFecha(x)==True and esFecha(y)==True

    año1 = int(x//10000)            #se extrae año
    año2 = int(y//10000)            #se extrae año
    
    mmdd1 = int(x%10000)             #en estas variables se guarda
    mmdd2 = int(y%10000)             #el mes y fecha (MMDD)

    if mmdd1==mmdd2:
        return abs(año1-año2)

    elif mmdd1>mmdd2:                   #como el numero MMDD comienza
        if año1>año2:                   #en 101 (1 de enero) y termina
            return abs(año1-año2)       #en 1231 (31 de diciembre) se pueden
        elif año1<año2:                 #comparar los 2 valores
            return abs(año1-año2)-1
        else:
            return 0
        
    elif mmdd1<mmdd2:
        if año1>año2:
            return abs(año1-año2)-1
        elif año1<año2:
            return abs(año1-año2)
        else:
            return 0

assert diferencia(20230820,19940114)==29
assert diferencia(20031128,20230821)==19

#escribir: int -> str
#Transforma una fecha indicada en una linea de texto con ella
#ej1: escribir(20031128) -> 28 noviembre 2003
#ej2: escribir(20230827) -> 27 agosto 2023
def escribir(x):
    assert esFecha(x)==True
    año = int(x//10000)
    mes = int((x%10000)//100) 
    dia = int(x%100)                    

    if mes==1:
        mes = 'enero'
    elif mes==2:
        mes = 'febrero'
    elif mes==3:
        mes = 'marzo'
    elif mes==4:
        mes = 'abril'
    elif mes==5:
        mes = 'mayo'
    elif mes==6:
        mes = 'junio'
    elif mes==7:
        mes = 'julio'
    elif mes==8:
        mes = 'agosto'
    elif mes==9:
        mes = 'septiembre'
    elif mes==10:
        mes = 'octubre'
    elif mes==11:
        mes = 'noviembre'
    elif mes==12:
        mes = 'diciembre'
        
    return print(dia,mes,año)
