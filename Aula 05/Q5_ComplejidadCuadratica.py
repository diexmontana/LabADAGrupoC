#Q5: Cual es la complejidad de
def imprimir(arr):
    # Muestra los elementos de un arreglo n veces
    # La primera vez muestra 0 elementos y en cada vuelta muestra un elemento más
    n = len(arr)
    for i in range(n):
        for j in range(i):
            print(arr[j])

arreglo = ["a","b","c","d","e"]
imprimir(arreglo)

# j: 0
# j: 0,1
# j: 0, 1, 2
# -> n(n+1) / 2
# Complejidad O(n^2)