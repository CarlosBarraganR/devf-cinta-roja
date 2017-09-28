#Encoding
# -*- coding: utf-8 -*-
"""
    createTxt(name, text)

    :param name
    name of the file
    :param text
    text inside the file

    Creates a txt file in root
"""
def createTxt(name, text):
    file = open(name, "w")
    file.write(text)
    file.close()

createTxt("prueba.txt", "Lorem ipsum")

