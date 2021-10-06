#Ejercicio 01

def binarySearch(arr, valor):
    #Dado un arreglo y un elemento
    #Busca el elemento dado en el arreglo

    inicio = 0
    final = len(arr) - 1

    while inicio <= final:
        medio = (inicio + final) // 2
        if arr[medio] == valor:
            return True
        elif arr[medio] < valor:
            inicio = medio + 1
        elif arr[medio] > valor:
            final = medio -1
    return False

arreglo = [2,4,8,9,10,22,25,26,28,29,30,42,45,56]

print(binarySearch(arreglo,22))
print(binarySearch(arreglo,24))










