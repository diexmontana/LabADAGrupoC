#Q1: Cual es la complejidad de
def imprimir(arr):
    # Muestra los elementos de las posiciones pares un arreglo
    n = len(arr)# O(1)
    for i in range(0, n, 2): #O(n)
        print(arr[i])
        
arreglo = ["a","b","c","d","e"]
imprimir(arreglo)

# i: 0, 2, 4 -> n/2 ->O(n)
# Complejidad O(n)