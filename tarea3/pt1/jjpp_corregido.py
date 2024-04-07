#listas con informacion
paises=[['01','Argentina',0,0,0],['02','Brasil',0,0,0],['03','Canadá',0,0,0],\
        ['04','Chile',0,0,0],['05','Colombia',0,0,0],['06','Jamaica',0,0,0],\
        ['07','México',0,0,0],['08','EEUU',0,0,0]]

deportes=[['101','Ciclismo Pista Masculino'],['102','Natación Masculino'],['103','Gimnasia Masculino'],\
          ['104','Tenis Masculino'],['201','Atletismo Femenino'],['202','Clavados Femenino']]

deportistas=[['1001','Guido Andreozzi','01'],    ['1002','Marcelo Chierighini','02'],['1003','Joao Menezes','02'],\
             ['1004','Elizabeth Gleadle','03'],  ['1005','Meaghan Benfeito','03'],   ['1006','Caeli Mckay','03'],\
             ['1007','Felipe Peñaloza','04'],    ['1008','Tomas Gonzalez','04'],     ['1009','Tomás Barrios','04'],\
             ['1010','Juan Esteban Arango','05'],['1011','Andres Martinez','05'],    ['1012','Shericka Jackson','06'],\
             ['1013','Ignacio Prado','07'],      ['1014','Miguel de Lara','07'],     ['1015','Paola Moran','07'],\
             ['1016','Alejadra Orozco','07'],    ['1017','Daniel Holloway','08'],    ['1018','Gavin Hoover','08'],\
             ['1019','Nathan Adrian','08'],      ['1020','Michael Chadwick','08'],   ['1021','Nathan Adrian','08'],\
             ['1022','Nicolas Fink','08'],       ['1023','Kara Winger','08'],        ['1024','Ariana Ince','08'],\
             ['1025','Courtney Okolo','08'],     ['1026','Robert Neff','08']]

competencias=[['2001','Omnium','101','1017','1013','1007'],\
              ['2002','Madison','101','1007','1018','1010'],\
              ['2003','100m libre','102','1002','1019','1020'],\
              ['2004','200m pecho','102','1019','1022','1014'],\
              ['2005','Piso','103','1008','1026','1011'],\
              ['2006','Individual','104','1003','1009','1001'],\
              ['2007','Lanz. de jabalina','201','1023','1004','1024'],\
              ['2008','400m planos','201','1012','1015','1025'],\
              ['2009','Plataforma 10m','202','1005','1006','1016']]

#[['01', 'Argentina', 0, 0, 1], ['02', 'Brasil', 2, 0, 0], ['03', 'Canadá', 1, 2, 0], \
#['04', 'Chile', 2, 1, 1], ['05', 'Colombia', 0, 0, 2], ['06', 'Jamaica', 1, 0, 0], \
#['07', 'México', 0, 2, 2], ['08', 'Estados Unidos', 3, 4, 3]]
#--------------------------------------

#buscar: str list(list) -> list
#lista de T cuyo primer valor es x (None si no existe)
#ej: buscar('xx',paises) -> ['xx','Chile',0,0,0]
#ej: buscar('xxxx',deportistas) -> ['xxxx','Isidora Jimenez','xx']
#ej: buscar('yyyy',competencias) -> None
def buscar(x,T):
    for L in T:
        if L[0]==x: return L
    return None

#buscarIndice: str list(list) -> int
#indice de lista de T cuyo primer valor es x (-1 si no existe)
#ej: buscarIndice('xx',paises) -> 0
#ej: buscarIndice('xxxx',deportistas) -> 0
#ej: buscarIndice('yyyy',competencias) -> -1
def buscarIndice(x,T):
    for i in range(len(T)):
        if T[i][0]==x: return i
    return -1


#calcular medallas de cada pais
def calcularMedallas():
    for comp in competencias:   
        paisoro=buscar(comp[3],deportistas)[2]
        paisplat=buscar(comp[4],deportistas)[2]
        paisbron=buscar(comp[5],deportistas)[2]
        for pais in paises:
            if pais[0]==paisoro:
                pais[2]+=1
            if pais[0]==paisplat:
                pais[3]+=1
            if pais[0]==paisbron:
                pais[4]+=1
    return paises


#mostrar medallero ordenado
def mostrarMedallero():
    paises_1=list(paises)
    def inverso(x):
        L=[x[2],x[3],x[4],x[0],x[1]]
        return L
    for i in range(len(paises_1)):
        paises_1[i]=inverso(paises_1[i])
    paises_1.sort()
    paises_1.reverse()
    for pais in paises_1:
        print(pais[0],pais[1],pais[2],(pais[0]+pais[1]+pais[2]),pais[4])


#mostrar informacion de un pais
def mostrarPais():
    cod_pa=str(input('Código país? '))
    pais=buscar(cod_pa, paises)
    if pais ==None:
        print('Codigo de país inválido')
    else:
        print('Nombre del País:', pais[1])
        print('Medallas de oro:', pais[2])
        print('Medallas de plata:', pais[3])
        print('Medallas de bronce:', pais[4])
        print('Total de medallas:', (pais[2]+pais[3]+pais[4]))
    
    

#mostrar informacion de un deporte
def mostrarDeporte():
    cod_dep=str(input('Código del deporte? '))
    dep=buscar(cod_dep,deportes)
    if dep==None:
        print("codigo de deporte inválido")
    else:
        print('Nombre del deporte:', dep[1])
        for comp in competencias:
            if comp[2]==cod_dep:
                print('-----')
                print('Nombre de la competencia:', comp[1])
                print('Deportista en primer lugar:')
                dept=buscar(comp[3], deportistas)
                print('Nombre: ', dept[1])
                paisdept=buscar(dept[2],paises)
                print('País: ', paisdept[1])
            

             

#mostrar informacion de un deportista
def mostrarDeportista():
    cod_dept=str(input('Código del deportista? '))
    dept=buscar(cod_dept, deportistas)
    if dept==None:
        print("codigo del deportista inválido")
    else:
        print('Nombre del deportista: ',dept[1])
        paisdept=buscar(dept[2],calcularMedallas())
        print('Nombre del país: ',paisdept[1])
        medoro=0
        medplat=0
        medbron=0
        for comp in competencias:
            if comp[3]==cod_dept:
                medoro += 1
            if comp[4]==cod_dept:
                medplat += 1
            if comp[5]==cod_dept:
                medbron += 1
        print('Medallas de oro: ',medoro)
        print('Medallas de plata: ',medplat)
        print('Medallas de bronce: ',medbron)


#mostrar informacion de una competencia
def mostrarCompetencia():
    cod_comp=str(input('Código de la competencia? '))
    comp=buscar(cod_comp,competencias)
    if comp==None:
        print("codigo de competencia inválido")
    else:
        print('Nombre de la competencia: ', comp[1])
        dep=buscar(comp[2],deportes)
        print('Nombre del deporte: ', dep[1])

        print('---')
        print('Primer Lugar')
        oro=buscar(comp[3],deportistas)
        print('Nombre: ', oro[1])
        paisoro=buscar(oro[2],paises)
        print('Pais: ', paisoro[1])

        print('---')
        print('Segundo Lugar')
        plat=buscar(comp[4],deportistas)
        print('Nombre: ', plat[1])
        paisplat=buscar(plat[2],paises)
        print('Pais: ', paisplat[1])

        print('---')
        print('Tercer Lugar')
        bronx=buscar(comp[5],deportistas)
        print('Nombre: ', bronx[1])
        paisbronx=buscar(bronx[2],paises)
        print('Pais: ', paisbronx[1])


#programa principal
calcularMedallas()
mostrarMedallero()
print('----------')
#leer y procesar consultas
print('Ingrese 1(pais), 2(deporte), 3(deportista), 4(Competencia), 0(Fin)')
consulta=input('1,2,3,4 o 0? ')
while consulta!='0':
    if consulta=='1':
        mostrarPais()
    elif consulta=='2':
        mostrarDeporte()
    elif consulta=='3':
        mostrarDeportista()
    elif consulta=='4':
        mostrarCompetencia()
    else:
        print('debe ingresar valores entre 0 y 4')
    print('----------')
    consulta=input('1,2,3,4 o 0? ')
