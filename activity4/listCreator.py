#Encoding
# -*- coding: utf-8 -*-

"""
    list_creator(size)

    :param size = max length of the list
"""
def list_creator(size):
    list = []
    for index in range(0, size):
        list.append(raw_input("Dato de la lista: "))
    print list

list_size = input("Inserta el tamaño de la lista a crear: ")
list_creator(list_size)