# -*- coding: utf-8 -*-
"""
@author: Vicenç
"""

def majuscules(lletra):
    if lletra >= "A" and lletra <= "Z":
        lletra = chr(ord(lletra) + 32)
    return lletra

def vocals(lletra):
    if lletra == "à" or lletra == "á" or lletra == "ä" or lletra == "â":
        lletra = "a"
    if lletra == "À" or lletra == "Á" or lletra == "Ä" or lletra == "Â":
        lletra = "a"
    
    if lletra == "è" or lletra == "é" or lletra == "ë" or lletra == "ê":
        lletra = "e"
    if lletra == "È" or lletra == "É" or lletra == "Ë" or lletra == "Ê":
        lletra = "e"
    
    if lletra == "ì" or lletra == "í" or lletra == "ï" or lletra == "î":
        lletra = "i"
    if lletra == "Ì" or lletra == "Í" or lletra == "Ï" or lletra == "Î":
        lletra = "i"
    
    if lletra == "ò" or lletra == "ó" or lletra == "ö" or lletra == "ô":
        lletra = "o"
    if lletra == "Ò" or lletra == "Ó" or lletra == "Ö" or lletra == "Ô":
        lletra = "o"
    
    if lletra == "ù" or lletra == "ú" or lletra == "ü" or lletra == "û":
        lletra = "a"
    if lletra == "Ù" or lletra == "Ú" or lletra == "Ü" or lletra == "Û":
        lletra = "u"
    return lletra

def excepcions(lletra, language):
    if lletra == "Ç" or lletra == "ç":
        if language == "frances" or language == "catala":
            lletra = "c"
    elif lletra == "Ñ":
        if language == "castella":
            lletra = "ñ"
            
    elif lletra == "œ" or lletra == "Œ":
        if language == "frances":
            lletra = "oe"
        
    elif lletra == "æ" or lletra == "Æ":
        if language == "frances":
            lletra = "ae"
        
    elif lletra == "ß":
        if language == "alemany":
            lletra = "ss"
    
    return lletra


fileName = "Rive.txt"
fileName2 = "Rive2.txt"
file = open(fileName, "r", encoding = "utf8")
fileWrite = open(fileName2, "x", encoding = "utf8")
language = input("Entra el llenguatge del text (angles, alemany, catala, castella, frances o italia): \n")

while True:
    lletra = file.read(1)
    if not lletra:
        break
    lletra = majuscules(lletra)
    lletra = vocals(lletra)
    lletra = excepcions(lletra, language)
    
    if (lletra >= "a" and lletra <= "z") or lletra == "ss" or lletra == "ae" or lletra == "oe" or lletra == "ñ" or lletra == " " or lletra == "\n":
        if language == "italia" and (lletra == "j" or lletra == "k" or lletra == "w" or lletra == "x" or lletra == "y"):
            pass
        else:
            fileWrite.write(lletra)


file.close()
fileWrite.close()







