# 1. greatestNumber.py
# Convertir la complejidad de O(n^2) a O(n)
def greatestNumber(array):
    # Encuentra el mayor número en el arreglo
    for i in array:
        isValTheGreatest = True
        for j in array:
            if j > i:
                isIValTheGreatest = False
        if isIValTheGreatest:
            return i

def greatestNumber2(array):
    for i in array:
        isValTheGreatest = i
        if (isValTheGreatest < i):
            isValTheGreatest = i
        
    return i


arreglo = [42,21,5,26,19,98]
print(greatestNumber2(arreglo))
