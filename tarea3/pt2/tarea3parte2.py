A=open('paises.txt','r')
paises=[]
pais=[]
for p in A:
    pais=[p[0:2],int(p[4:5]),int(p[7:8]),int(p[10:11]),p[11:len(p)-1]]
    
    paises+=[pais]
A.close()

A=open('deportes.txt','r')
deportes=[]
deporte=[]
for dp in A:
    deporte=[dp[0:3],dp[3:len(dp)-1]]
    
    deportes+=[deporte]
A.close()

A=open('deportistas.txt','r')
deportistas=[]
depta=[]
for dept in A:
    depta=[dept[0:4],dept[4:6],dept[6:len(dept)-1]]
    
    deportistas+=[depta]
A.close()

A=open('competencias.txt','r')
competencias=[]
compet=[]
for comp in A:
    compet=[comp[0:4],comp[4:7],comp[7:11],comp[11:15],comp[15:19],comp[19:len(comp)-1]]
    
    competencias+=[compet]
A.close()

#--------------------------# funciones ocupadas en tarea 3 parte 1

def buscar(x,T):
    for L in T:
        if L[0]==x: return L
    return None

def buscarIndice(x,T):
    for i in range(len(T)):
        if T[i][0]==x: return i
    return -1

#--------------------------#

cod_comp=input('Cuál es el código de la competencia? ')
while cod_comp!='.':
    comp=buscar(cod_comp,competencias)
    if comp==None:
        print('Código de competencia inválido')

    print('Nombre de la competencia:',comp[5])
    print('Nombre del deporte:',buscar(comp[1],deportes)[1])

    #--ORO--
    oro=input('Cual es el número del deportista que obtuvo med. de oro? ')
    dept=buscar(oro,deportistas)
    if dept==None:
        print('Deportista no existe')
    comp[2]=oro
    print('Nombre del deportista:',dept[2])
    print('Pais del deportista:',buscar(dept[1],paises)[4])
    paisoro=dept[1]
    if paisoro!=None:
        for pais in paises:
            if pais[0]==paisoro:
                pais[1]+=1
    
    #--PLATA--
    plata=input('Cual es el número del deportista que obtuvo med. de plata? ')
    dept=buscar(plata,deportistas)
    if dept==None:
        print('Deportista no existe')
    comp[3]=plata
    print('Nombre del deportista:',dept[2])
    print('Pais del deportista:',buscar(dept[1],paises)[4])
    paisplat=dept[1]
    if paisplat!=None:
        for pais in paises:
            if pais[0]==paisplat:
                pais[2]+=1

    #--BRONCE--
    bronce=input('Cual es el número del deportista que obtuvo med. de bronce? ')
    dept=buscar(bronce,deportistas)
    if dept==None:
        print('Deportista no existe')
    comp[4]=bronce
    print('Nombre del deportista:',dept[2])
    print('Pais del deportista:',buscar(dept[1],paises)[4])
    paisbron=dept[1]
    if paisbron!=None:
        for pais in paises:
            if pais[0]==paisbron:
                pais[3]+=1

    print('----------')
    cod_comp=input('Cuál es el código de la competencia? ')

#----------------------------------------------------#

#trescc: int -> str
#convierte numero a un string de 3 caracteres
#ej: trescc(12) -> "012"
def trescc(numero):
  s=str(numero)
  n=len(s)
  if n<3: s=' '*(3-n)+s
  return s

B=open('competencias.txt', 'w')
for comp in competencias:
    B.write(comp[0]+comp[1]+comp[2]+comp[3]+comp[4]+comp[5]+'\n')
B.close()

C=open('paises.txt','w')
paises_1=list(paises)
def inverso(x):
    L=[x[1],x[2],x[3],x[4],x[0]]
    return L
for i in range(len(paises_1)):
    paises_1[i]=inverso(paises_1[i])
paises_1.sort()
paises_1.reverse()
for p in paises_1:
    C.write(p[4]+trescc(p[0])+trescc(p[1])+trescc(p[2])+p[3]+'\n')
C.close()


