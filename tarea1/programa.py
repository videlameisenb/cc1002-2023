from fecha import *

fe1 = int(input('Fecha1? '))
if not esFecha(fe1):
    print ('Fecha Incorrecta')
else:
    escribir(fe1)
    fe2 = int(input('Fecha2? '))
    if not esFecha(fe2):
        print ('Fecha Incorrecta')
    else:
        escribir(fe2)
        fe3 = int(input('Fecha3? '))
        if not esFecha(fe3):
            print ('Fecha Incorrecta')
        else:
            escribir(fe3)
            if fe1>fe2 and fe1>fe3:
                p1=fe1
                if fe2>fe3:
                    p2=fe2
                    p3=fe3
                else:
                    p2=fe3
                    p3=fe2
            if fe2>fe1 and fe2>fe3:
                p1=fe2
                if fe1>fe3:
                    p2=fe1
                    p3=fe3
                else:
                    p2=fe3
                    p3=fe1
            if fe3>fe1 and fe3>fe2:
                p1=fe3
                if fe1>fe2:
                    p2=fe1
                    p3=fe2
                else:
                    p2=fe2
                    p3=fe1

            print('Ordenadas de menor a mayor: ')
            escribir(p3)
            escribir(p2)
            escribir(p1)


