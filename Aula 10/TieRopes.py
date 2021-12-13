# TieRopes.py

def tieRopes(K, A):
    # Devuelve el numero de sogas atadas o no
    # que son mayores o iguales a k
    numSogas = 0
    largo = 0
    for i in A:
        largo += i  # Se van atando sumando los largos
        if largo >= K: 
            numSogas += 1
            largo = 0
    return numSogas

print(tieRopes(4, [1, 2, 3, 4, 1, 1, 3]))