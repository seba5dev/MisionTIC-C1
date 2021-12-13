print("Hola, mundo")

#python no tiene corchetes utiliza indentacion
if 5 > 2:
    print("Cinco es mayor que dos")

#variables
x = 5 #int
y = "Hola, mundo" #string

#variables especificas
x = str(3) #string
y = int(5) #int
z = float(5) #float

#conseguir tipo de variable
print(type(x))
print(type(y))

#asignar multiples variables
x, y, z = "Naranja", "Banana", "Cereza"
print(x)
print(y)
print(z)

#asignar un valor a multiples variables
x = y = z = "Naranja"
print(x)
print(y)
print(z)

#desempaquetar colecciones
frutas = ["Manzana", "Banana", "Cereza"]
x, y, z = frutas
print(x)
print(y)
print(z)

#mostrar variables
x = "asombroso"
print("Python es " + x)
x = "Python es "
y = "asombroso"
z =  x + y
print(z)

#crear variables globales
x = "asombroso"
def funcion():
    print("Python es " + x)
funcion()

#usar la variable global para usar una variable de funcion como global
def funcion():
    global x
    x = "asombroso"
funcion()
print("Python es " + x)

