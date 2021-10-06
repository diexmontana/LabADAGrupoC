#Ejercicio 01

def matrBinSearch(matriz, valor):
    #Dada una matriz ordenada y un elemento
    #Busca el elemento dado en la matriz

    rows = len(matriz)
    cols = len(matriz[0])
    inicio = 0
    final = rows * cols - 1
    

    while inicio <= final:
        medio = (inicio + final) // 2
        x = medio // cols 
        y = medio - (x * 3)
        if matriz[x][y] == valor:
            return True
        elif matriz[x][y] < valor:
            inicio = medio + 1
        elif matriz[x][y] > valor:
            final = medio -1
    return False

matriz = [[1, 3, 5], [7, 9, 11], [13, 15, 17]]

print(matrBinSearch(matriz,7))
print(matrBinSearch(matriz,11))
print(matrBinSearch(matriz,12))