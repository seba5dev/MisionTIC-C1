import numpy as np

def Menu():
    opcion = int(input("Menu Principal" + "\n" + "1. Ver listado" + "\n" + "2. Ver listado filtrado" + "\n" + "3. Agregar beneficiario" + "\n" + "4. Buscar beneficiario" + "\n" + "5. Borrar beneficiario"  + "\n" + "6. Salir" + "\n"))
    return opcion


def Crear():
    archivo = open("agenda.txt","a")
    print("Digite la información del beneficiario a agregar:")
    usuario = ["","",""]
    usuario[0] = str(input())        
    usuario[1] = str(input())   
    usuario[2] = str(input())   
    for element in usuario:
        archivo. write(element + "\n")
    print("El beneficiario ha sido agregado")
    archivo.close()  
        
def Leer():
    print("Listado de beneficiarios")
    archivo = open("agenda.txt" , "r")
    print(archivo.read())
    archivo.close()  

def LeerFiltrado(letra):
    count = 0
    print("Listado filtrado de beneficiarios:")
    archivo = open("agenda.txt" , "r")
    lineas = archivo.readlines()
    for line in lineas:
        palabras = line.split(' ')
        palabra = "".join(palabras)
        if palabra[0] == letra:
            data =  lineas[count:(count + 3)]
            for element in data:
                print(element.replace("\n",""))
        count += 1


def Buscar(nombre):
    count = 0
    IsEmpty = True
    archivo = open("agenda.txt" , "r")
    lineas = archivo.readlines()
    for line in lineas:
        palabra =  line.replace("\n","")
        if palabra == nombre:
            IsEmpty = False
            data =  lineas[count:(count + 3)]
            for element in data:
                print(element.replace("\n",""))
    if(IsEmpty):
        print("No se encuentra el beneficiario en la agenda")

def Eliminar(cedula):
    data = np.genfromtxt("agenda.txt",delimiter='\t', dtype=str)
    divider= data.size/3
    data = np.split(data,divider)
    count = 0
    for objeto in data:
        if cedula in objeto:
            data = np.delete(data,count,0)
        count += 1
    archivo = open("agenda.txt","w")
    for element in data:
       for element1 in element:
           archivo.write(element1 + "\n")
    print("El usuario ha sido eliminado del listado")
    archivo.close()  

while(True):
    opcionD = Menu()
    if (opcionD == 1):
        Leer()
    elif (opcionD == 2):
        letra = input("Digite la letra por la que empiezan los beneficiarios:")
        LeerFiltrado(letra)
    elif (opcionD == 3):
        Crear()
    elif (opcionD == 4):
        nombre = input("Digite el nombre y apellido del beneficiario a buscar:")
        Buscar(nombre)
    elif (opcionD == 5):
        cedula = input("Digite la cedula del beneficiario a borrar:")
        Eliminar(cedula)
    elif (opcionD == 6):
        print("Hasta pronto")
        pass
        break