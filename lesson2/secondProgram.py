#Encoding
# -*- coding: utf-8 -*-

# #Funcion
# def saludar(name, message="Hola"):
#     print message, name
#
# #Funciones recursivas
# def play(intento=1):
#     respuesta = raw_input("¿De que color es una naranja? ")
#     if respuesta != "naranja":
#         if intento < 3:
#             print "\n Fallaste, intenta de nuevo"
#             intento +=1
#             play(intento) #Llamada Recursiva
#         else:
#             print  "\nPerdiste!"
#     else:
#         print "\nGanaste\n"
#
#
# play()

#Asignacion Multiple
def printing():
    a, b, c = 'string', 15, True
    mi_tupla = ('hola mundo', 2014)
    texto, anio = mi_tupla
    print str(a)
    print str(b)
    print str(c)
    print str(texto)
    print str(anio)


#printing()


#While

def the_while():
    while True:
        name = raw_input("Escribe su nombre: ")
        if name:
            print name
            break


#the_while()

#For
def the_for():
    mi_lista = ["Juan", "Antonio", "Pepe", "Julio"]
    for nombre in mi_lista:
        print nombre
    mi_tupla = ["Azul", "Rojo", "Verde", "Amarillo"]
    for color in mi_tupla:
        print color
    for anio in range(2001,2013):
        print anio

#the_for()



# def iniciar():
#     dulce = raw_input("Elija Letra: ")
#     if dulce == "a":
#         precio = 2.5
#         print "Tu Cambio: ", calcularVuelto(monto, precio)
#     elif dulce == "b"
#         precio == "10"
#         print "Tu Cambio: ", calcularVuelto(monto,precio)

