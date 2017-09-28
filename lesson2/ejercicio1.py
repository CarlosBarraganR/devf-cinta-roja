#Encoding
# -*- coding: utf-8 -*-

"""
    calcula_cambio(money,precio) -> int or string

    Calculates the money left after buying a product and validates if the money is enough to buy the selected product
"""
def calcula_cambio(money, precio):
    if money >= precio:
        return money - precio
    else:
        return "El monto que ingresaste es menor que el precio del producto"


"""
    select_product(money,producto) -> none
    
    A filter for the selected product and gives back the change if it is the case
"""
def select_product(money, producto):
    if producto == 1:
        print "Seleccionaste panditas"
        print "Tu cambio es de: $" + str(calcula_cambio(money, precio=2.50))
    elif producto == 2:
        print "Seleccionaste Chocorroles"
        print "Tu cambio es de: $" + str(calcula_cambio(money, precio=1.50))
    elif producto == 3:
        print "Seleccionaste Chocorroles"
        print "Tu cambio es de: $" + str(calcula_cambio(money, precio=4.00))
    elif producto == 4:
        print "Seleccionaste Chocorroles"
        print "Tu cambio es de: $" + str(calcula_cambio(money, precio=1.2))


"""
    vending_machine() -> none

    Main function for the vending machine
"""
def vending_machine():
    print "Tenemos los siguientes productos:\n1) Panditas: $2.50\n2) Chochorroles: $1.40\n3) Mentas: $4.00\n4) Cafe: $1.20"
    money = input("Ingresa tu dinero (Solo aceptamos monedas menores a $5.00:) ")
    if money < 5:
        print "Ingresaste: $" + str(money)
        producto = input("Seleciona el producto que quieras comprar: ")
        select_product(money, producto)

    else:
        print "Error, no se puede ingresar mas de 5 Pesos"

vending_machine()