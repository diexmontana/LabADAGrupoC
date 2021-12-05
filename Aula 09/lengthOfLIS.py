# lengthOfLIS.py Number of Longest Increasing Subsequence

def lengthOfLIS(nums):
    # Dado una lista de enteros: nums, devuelve la más extensa subsecuencia creciente de nums

    # Crearemos una lista de subsecuencias: listaSubs donde cada posición indica la más extensa subsecuencia hasta esa posición
    # Primero creamos una lista de unos que será la lista inicial de subsecuncias
    listaSub = [1] * len(nums)
    
    
    for i in range(len(nums)):
        # Comparamos la posición actual de nums con sus anteriores posiciones
        for j in range (i):
            # Si la posición actual de nums es mayor que la anterior hay una nueva subsecuencia
            # En listaSub incrementamos en uno al valor de la posición anterior de listaSub
            # Se escoje entre el nuevo valor o el que ya se tenia de la posición actual
            if  nums[i] > nums[j]:
                listaSub[i] = max(listaSub[i], listaSub[j] + 1)
    print(listaSub)
    return max(listaSub)

lista1 = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(lista1))