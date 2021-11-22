# Backspace.py

from collections import deque

def backSpace(cadena):
    # Recibe una cadena y elimina un caracter por cada #
    # Se elimina de derecha a izquierda
    queue = deque()
    for x in cadena:
        if x == "#":
            queue.pop()
        else:
            queue.append(x)
    return queue

print(backSpace("abc#de##f#ghi#jklmn#op#"))