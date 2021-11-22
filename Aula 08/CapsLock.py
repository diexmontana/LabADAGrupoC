# CapsLock.py

from collections import deque

def capsLock(cadena):
    # recibe una cadena y devuelve otra modificada
    # todo los caracteres antes de $ se  almacenanan en el resultado
    # cuando el caracter es @ capslock se activa
    # en capslock activo las mayusculas y minusculas se intercambian
    queue = deque(cadena)
    wordA = ""
    wordB = ""
    capsLock = False
    for i in queue:
        if i == "$":
            wordA = wordA + wordB
            wordB=""
        elif i == "@":
            if capsLock == False:
                wordB = wordB.swapcase()
            capsLock = not capsLock
        elif capsLock == False:
            wordB = wordB + i
        else:
            wordB = wordB + i.swapcase()
        
    return wordA

print(capsLock("abc$d@ef@g$"))
print(capsLock("abc$d@ef$@g$"))
    
