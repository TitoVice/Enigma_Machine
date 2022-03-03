# -*- coding: utf-8 -*-
"""
@author: Vicenç
"""

''' ROTORS '''

'''
He copiat l'ordre dels rotors originals, canviant-ho una mica, he hagut de fer un 
set de rotors per cada llengua amb diferent numero de caracters.
'''
   
rotor1General = {0:"b", 1:"g", 2:"d", 3:"q", 4:"o", 5:"h", 6:"u", 7:"s", 8:"c", 9:"a", 
          10:"m", 11:"i", 12:"f", 13:"r", 14:"v", 15:"t", 16:"p", 17:"n", 18:"e", 
          19:"z", 20:"l", 21:"j", 22:"k", 23:"w", 24:"x", 25:"y"}

rotor2General = {0:"n", 1:"t", 2:"z", 3:"p", 4:"s", 5:"f", 6:"b", 7:"o", 8:"g", 9:"m", 
          10:"h", 11:"r", 12:"c", 13:"q", 14:"d", 15:"i", 16:"v", 17:"l", 18:"a", 
          19:"e", 20:"u", 21:"y", 22:"x", 23:"w", 24:"k", 25:"j"}

rotor3General = {0:"f", 1:"v", 2:"i", 3:"u", 4:"b", 5:"h", 6:"t", 7:"c", 8:"d", 9:"l", 
          10:"a", 11:"m", 12:"e", 13:"q", 14:"z", 15:"p", 16:"o", 17:"s", 18:"g", 
          19:"r", 20:"n", 21:"x", 22:"k", 23:"w", 24:"j", 25:"y"}

rotor4General = {0:"q", 1:"r", 2:"h", 3:"o", 4:"g", 5:"n", 6:"e", 7:"c", 8:"v", 9:"p", 
          10:"u", 11:"z", 12:"t", 13:"f", 14:"d", 15:"b", 16:"a", 17:"s", 18:"l", 
          19:"m", 20:"i", 21:"k", 22:"x", 23:"y", 24:"j", 25:"w"}

rotor5General = {0:"q", 1:"v", 2:"e", 3:"r", 4:"t", 5:"z", 6:"u", 7:"i", 8:"o", 9:"a", 
          10:"s", 11:"d", 12:"f", 13:"g", 14:"h", 15:"b", 16:"l", 17:"p", 18:"m", 
          19:"n", 20:"c", 21:"w", 22:"j", 23:"x", 24:"y", 25:"k"}


rotor1It = {0:"b", 1:"g", 2:"d", 3:"q", 4:"o", 5:"h", 6:"u", 7:"s", 8:"c", 11:"a", 
          12:"m", 13:"i", 14:"f", 15:"r", 16:"v", 17:"t", 18:"p", 19:"n", 20:"e", 
          21:"z", 25:"l"}

rotor2It = {0:"n", 1:"t", 2:"z", 3:"p", 4:"s", 5:"f", 6:"b", 7:"o", 8:"g", 11:"m", 
          12:"h", 13:"r", 14:"c", 15:"q", 16:"d", 17:"i", 18:"v", 19:"l", 20:"a", 
          21:"e", 25:"u"}

rotor3It = {0:"f", 1:"v", 2:"i", 3:"u", 4:"b", 5:"h", 6:"t", 7:"c", 8:"d", 11:"l", 
          12:"a", 13:"m", 14:"e", 15:"q", 16:"z", 17:"p", 18:"o", 19:"s", 20:"g", 
          21:"r", 25:"n"}

rotor4It = {0:"q", 1:"r", 2:"h", 3:"o", 4:"g", 5:"n", 6:"e", 7:"c", 8:"v", 11:"p", 
          12:"u", 13:"z", 14:"t", 15:"f", 16:"d", 17:"b", 18:"a", 19:"s", 20:"l", 
          21:"m", 25:"i"}

rotor5It = {0:"q", 1:"v", 2:"e", 3:"r", 4:"t", 5:"z", 6:"u", 7:"i", 8:"o", 11:"a", 
          12:"s", 13:"d", 14:"f", 15:"g", 16:"h", 17:"b", 18:"l", 19:"p", 20:"m", 
          21:"n", 25:"c"}


rotor1Esp = {0:"b", 1:"g", 2:"d", 3:"q", 4:"o", 5:"h", 6:"u", 7:"s", 8:"c", 9:"a", 
          10:"m", 11:"i", 12:"f", 13:"r", 14:"v", 15:"t", 16:"p", 17:"n", 18:"e", 
          19:"z", 20:"l", 21:"ñ", 22:"k", 23:"w", 24:"x", 25:"y", 26:"j"}

rotor2Esp = {0:"n", 1:"t", 2:"z", 3:"p", 4:"s", 5:"f", 6:"b", 7:"ñ", 8:"g", 9:"m", 
          10:"h", 11:"r", 12:"c", 13:"q", 14:"d", 15:"i", 16:"v", 17:"l", 18:"a", 
          19:"e", 20:"u", 21:"y", 22:"x", 23:"w", 24:"k", 25:"j", 26:"o"}

rotor3Esp = {0:"f", 1:"v", 2:"i", 3:"u", 4:"b", 5:"h", 6:"t", 7:"c", 8:"ñ", 9:"l", 
          10:"a", 11:"m", 12:"e", 13:"q", 14:"z", 15:"p", 16:"o", 17:"s", 18:"g", 
          19:"r", 20:"n", 21:"x", 22:"k", 23:"w", 24:"j", 25:"y", 26:"d"}

rotor4Esp = {0:"q", 1:"r", 2:"h", 3:"o", 4:"g", 5:"ñ", 6:"e", 7:"c", 8:"v", 9:"p", 
          10:"u", 11:"z", 12:"t", 13:"f", 14:"d", 15:"b", 16:"a", 17:"s", 18:"l", 
          19:"m", 20:"i", 21:"k", 22:"x", 23:"y", 24:"j", 25:"w", 26:"n"}

rotor5Esp = {0:"q", 1:"v", 2:"e", 3:"r", 4:"t", 5:"z", 6:"u", 7:"i", 8:"o", 9:"a", 
          10:"s", 11:"d", 12:"f", 13:"g", 14:"ñ", 15:"b", 16:"l", 17:"p", 18:"m", 
          19:"n", 20:"c", 21:"w", 22:"j", 23:"x", 24:"y", 25:"k", 26:"h"}

rotorsElegits = []
posR1 = 0
posR2 = 0
posR3 = 0

def eleccioRotors(nAlfabet):
    print("Ara tria quins 3 rotors utilitzar dels 5 (EX: r1): \n")
    if nAlfabet == 26:
        for n in range(3):
            rotor = input()
            if rotor == "r1":
                rotorsElegits.append(rotor1General)
            elif rotor == "r2":
                rotorsElegits.append(rotor2General)
            elif rotor == "r3":
                rotorsElegits.append(rotor3General)
            elif rotor == "r4":
                rotorsElegits.append(rotor4General)
            elif rotor == "r5":
                rotorsElegits.append(rotor5General)
    elif nAlfabet == 27:
        for n in range(3):
            rotor = input()
            if rotor == "r1":
                rotorsElegits.append(rotor1Esp)
            elif rotor == "r2":
                rotorsElegits.append(rotor2Esp)
            elif rotor == "r3":
                rotorsElegits.append(rotor3Esp)
            elif rotor == "r4":
                rotorsElegits.append(rotor4Esp)
            elif rotor == "r5":
                rotorsElegits.append(rotor5Esp)
    elif nAlfabet == 21:
        for n in range(3):
            rotor = input()
            if rotor == "r1":
                rotorsElegits.append(rotor1It)
            elif rotor == "r2":
                rotorsElegits.append(rotor2It)
            elif rotor == "r3":
                rotorsElegits.append(rotor3It)
            elif rotor == "r4":
                rotorsElegits.append(rotor4It)
            elif rotor == "r5":
                rotorsElegits.append(rotor5It)
            
    print("Elegeix la posicio inicial de cada rotor, respectivament. Màxim: "+ str(nAlfabet))
    
    rotor1 = {}
    rotor2 = {}
    rotor3 = {}
    posR1 = int(input()) - 1
    posR2 = int(input()) - 1
    posR3 = int(input()) - 1
    
    for n in range(nAlfabet):
        aux1 = posR1 + n
        aux2 = posR2 + n
        aux3 = posR3 + n
        
        if aux1 > nAlfabet-1: aux1 -= nAlfabet
        if aux2 > nAlfabet-1: aux2 -= nAlfabet
        if aux3 > nAlfabet-1: aux3 -= nAlfabet
        
        rotor1[n] = rotorsElegits[0][aux1]
        rotor2[n] = rotorsElegits[1][aux2]
        rotor3[n] = rotorsElegits[2][aux3]
    
    rotorsElegits[0] = rotor1
    rotorsElegits[1] = rotor2
    rotorsElegits[2] = rotor3
        

def rotar(rotor):
    for n in range(nAlfabet-1):
        x = rotor[n]
        y = rotor[n+1]
        rotor[n] = y
        rotor[n+1] = x

def rotacio(lletra, posR1, posR2, posR3):
    "ROTACIÓ"
    posR1 += 1
    rotar(rotorsElegits[0])
    if posR1 > nAlfabet-1:
        posR1 = 0
        posR2 += 1
        rotar(rotorsElegits[1])
        if posR2 > nAlfabet-1:
            posR2 = 0
            posR3 += 1
            rotar(rotorsElegits[2])
            if posR3 > nAlfabet-1:
                posR3 = 0
                
    "ANADA"
    for r in rotorsElegits:
        if lletra == "ñ":
            lletra = r[26]
        else: 
            lletra = r[ord(lletra)-97]
    
    "REFLECTOR"
    if nAlfabet == 21:
        lletra = reflectorIt[lletra]
    elif nAlfabet == 27:
        lletra = reflectorEsp[lletra]
    else:
        lletra = reflector[lletra]
    
    "TORNADA"
    for n in rotorsElegits[2]:
        if lletra == rotorsElegits[2][n]:
            if n == 26:
                lletra = "ñ"
            else:
                lletra = chr(n+97)
            break
        
    for n in rotorsElegits[1]:
        if lletra == rotorsElegits[1][n]:
            if n == 26:
                lletra = "ñ"
            else:
                lletra = chr(n+97)
            break

    for n in rotorsElegits[0]:
        if lletra == rotorsElegits[0][n]:
            if n == 26:
                lletra = "ñ"
            else:
                lletra = chr(n+97)
            break

    return lletra, posR1, posR2, posR3

''' PLUGBOARD '''
''' registra els canvis que es facin en el plugboard '''

plugBoard = { "a":"a", "b":"b", "c":"c", "d":"d", "e":"e", "f":"f", "g":"g", 
             "h":"h", "i":"i", "j":"j", "k":"k", "l":"l", "m":"m", "n":"n", 
             "ñ":"ñ", "o":"o", "p":"p", "q":"q", "r":"r", "s":"s", "t":"t", 
             "u":"u", "v":"v", "w":"w", "x":"x", "y":"y", "z":"z", "ñ":"ñ" }
    

def plugEnter(nAlfabet):
    maxim = int(nAlfabet/2)
    
    print("Entra la combinació de plugs, màxim de: "+str(maxim)+" EX: a b\n")
    print("Acaba posant X \n")
    
    plug = ""
    for i in range(maxim):
        plug = input()
        if plug == "X":
            break
        plugBoard[plug[0]] = plug[2]
        plugBoard[plug[2]] = plug[0]



''' RFLECTOR '''
reflector = { "a":"b", "b":"a", "c":"d", "d":"c", "e":"f", "f":"e", "g":"h", 
             "h":"g", "i":"j", "j":"i", "k":"l", "l":"k", "m":"n", "n":"m", 
             "o":"p", "p":"o", "q":"r", "r":"q", "s":"t", "t":"s", 
             "u":"v", "v":"u", "w":"x", "x":"w", "y":"z", "z":"y" }

reflectorIt = { "a":"b", "b":"a", "c":"d", "d":"c", "e":"f", "f":"e", "g":"h", 
             "h":"g", "i":"l", "l":"i", "m":"n", "n":"m", 
             "o":"p", "p":"o", "q":"r", "r":"q", "s":"t", "t":"s", 
             "u":"v", "v":"u", "z":"z" }

reflectorEsp = { "a":"b", "b":"a", "c":"d", "d":"c", "e":"f", "f":"e", "g":"h", 
                 "h":"g", "i":"j", "j":"i", "k":"l", "l":"k", "m":"n", "n":"m", 
                 "o":"p", "p":"o", "q":"r", "r":"q", "s":"t", "t":"s", 
                 "u":"v", "v":"u", "w":"x", "x":"w", "y":"z", "z":"y", "ñ":"ñ"}


''' MAIN '''

fileName = input("Entra el nom del text: \n")
fileName2 = input("Entra el nom del fitxer de sortida: \n")
nAlfabet = int(input("Entra el numero de lletres de l'alfabet de la llengua corresponent: \n"))
plugEnter(nAlfabet)
eleccioRotors(nAlfabet)

file = open(fileName, "r", encoding = "utf8")
fileWrite = open(fileName2, "x", encoding = "utf8")

while True:
    lletra = file.read(1)
    if not lletra:
        break

    if lletra != " " and lletra != "\n":
        lletra = plugBoard[lletra]
        lletra, posR1, posR2, posR3 = rotacio(lletra, posR1, posR2, posR3)
        lletra = plugBoard[lletra]
    
    fileWrite.write(lletra)
        
file.close()
fileWrite.close()




















