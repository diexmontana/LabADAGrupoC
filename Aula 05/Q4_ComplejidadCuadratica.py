#Q4: Cual es la complejidad de
def imprimir(arr):
    # Imprime todos los elementos de un arreglo n veces
    n = len(arr) # O(1)
    for i in range(n): # O(n^2)
        for j in range(n): # O(n)
            print(arr[j])

arreglo = ["a","b","c","d","e"]
imprimir(arreglo)

# Complejidad O(n^2)