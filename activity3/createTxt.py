#Encoding
# -*- coding: utf-8 -*-

def createTxt(name, text):
    file = open(name, "w")
    file.write(text)
    file.close()

createTxt("prueba.txt", "Lorem ipsum")

