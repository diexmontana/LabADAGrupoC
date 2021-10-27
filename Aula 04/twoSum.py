# 3. twoSum
# Analizar la complejidad del código:
def twoSum(array): # O(n^2)
    # Retorana verdadero si los valores de dos posiciones diferentes suman 10
    for i in range(len(array)): # O(n^2) <- n*n 
        for j in range(len(array)): # O(n)
            if i != j and array[i] + array[j] == 10:
                return True
    return False

arreglo = [1,4,8,2]
twoSum(arreglo)