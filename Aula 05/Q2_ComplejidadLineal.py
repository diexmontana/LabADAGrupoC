#Q2: Cual es la complejidad de
def imprimir(arr):
    # Muestra todos los elementos de un arreglo en orden inverso
    n = len(arr)# O(1)
    for i in reversed(range(n)):# O(n)
        print(arr[i])

arreglo = ["a","b","c","d","e"]
imprimir(arreglo)

# La complejidad es O(n)