#listas con informacion
paises=[['xx','Chile',0,0,0]]
deportes=[['xxx','Atletismo Damas']]
deportistas=[['xxxx','Isidora Jimenez','xx']]
competencias=[['xxxx','100 metros','xxx','xxxx','xxxx','xxxx']]

#buscar: str list(list) -> list
#lista de T cuyo primer valor es x (None si no existe)
#ej: buscar('xx',paises) -> ['xx','Chile',0,0,0]
#ej: buscar('xxxx',deportistas) -> ['xxxx','Isidora Jimenez','xx']
#ej: buscar('yyyy',competencias) -> None
def buscar(x,T):
    for L in T:
        if L[0]==x: return L
    return None
assert buscar('xx',paises)==['xx','Chile',0,0,0]
assert buscar('xxxx',deportistas)==['xxxx','Isidora Jimenez','xx']
assert buscar('yyyy',competencias)==None

#buscarIndice: str list(list) -> int
#indice de lista de T cuyo primer valor es x (-1 si no existe)
#ej: buscarIndice('xx',paises) -> 0
#ej: buscarIndice('xxxx',deportistas) -> 0
#ej: buscarIndice('yyyy',competencias) -> -1
def buscarIndice(x,T):
    for i in range(len(T)):
        if T[i][0]==x: return i
    return -1
assert buscarIndice('xx',paises)==0
assert buscarIndice('xxxx',deportistas)==0
assert buscarIndice('yyyy',competencias)==-1

#calcular medallas de cada pais
def calcularMedallas():

#mostrar medallero ordenado
def mostrarMedallero():

#mostrar informacion de un pais
def mostrarPais(): 

#mostrar informacion de un deporte
def mostrarDeporte(): 

#mostrar informacion de un deportista
def mostrarDeportista(): 

#mostrar informacion de una competencia
def mostrarCompetencia(): 

#programa principal
calcularMedallas()
mostrarMedallero()
#leer y procesar consultas
print('Ingrese 1(pais), 2(deporte), 3(deportista), 4(Competencia), 0(Fin)')
consulta=input('1,2,3,4 o 0?')
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
    consulta=input('1,2,3,4 o 0?')


