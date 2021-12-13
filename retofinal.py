import numpy as np

def Menu():
    opcion = int(input("Menu principal" +"\n" + "1. Ver listado" + "\n" + "2. Ver listado filtrado" + "\n" + "3. Agregar beneficiario" + "\n" + "4. Buscar beneficiario" + "\n" + "5. Borrar beneficiario"  + "\n" + "6. Salir" + "\n \n"))
    return opcion

# OPCION 1
def LeerArchivo():
    print("Listado de beneficiarios")
    archivo = open("agenda.txt" , "r")
    print(archivo.read())
    archivo.close()

# OPCION 2
def LeerArchivoFiltrado(letra):
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

# OPCION 3
def CrearBenef():
    archivo = open("agenda.txt","a")
    print("Digite la información del beneficiario a agregar:")
    benef = ["","",""]
    benef[0] = str(input())        
    benef[1] = str(input())   
    benef[2] = str(input())   
    for element in benef:
        archivo. write(element + "\n")
    print("El beneficiario ha sido agregado")
    archivo.close()

# OPCION 4
def BuscarBenef(nombre):
    cont = 0
    noexiste = True
    archivo = open("agenda.txt" , "r")
    lineas = archivo.readlines()
    for line in lineas:
        palabra =  line.replace("\n","")
        if palabra == nombre:
            noexiste = False
            data =  lineas[cont:(cont + 3)]
            for element in data:
                print(element.replace("\n",""))
    if(noexiste):
        print("No se encuentra el beneficiario en la agenda")

# OPCION 5
def EliminarBenef(cedula):
    data = np.genfromtxt("agenda.txt",delimiter='\t', dtype=str)
    divider= data.size/3
    data = np.split(data,divider)
    cont = 0
    for objeto in data:
        if cedula in objeto:
            data = np.delete(data,cont,0)
        cont += 1
    archivo = open("agenda.txt","w")
    for elements in data:
       for element in elements:
           archivo.write(element + "\n")
    print("El usuario ha sido eliminado del listado")
    archivo.close()

# MENU
while(True):
    opc = Menu()
    if (opc == 1):
        LeerArchivo()
        print("\n")
    elif (opc == 2):
        letra = input("Digite la letra por la que empiezan los beneficiarios:")
        print("\n")
        LeerArchivoFiltrado(letra)
    elif (opc == 3):
        CrearBenef()
        print("\n")
    elif (opc == 4):
        nombre = input("Digite el nombre y apellido del beneficiario a buscar:")
        print("\n")
        BuscarBenef(nombre)
    elif (opc == 5):
        cedula = input("Digite la cedula del beneficiario a borrar:")
        print("\n")
        EliminarBenef(cedula)
    elif (opc == 6):
        print("Hasta pronto")
        break