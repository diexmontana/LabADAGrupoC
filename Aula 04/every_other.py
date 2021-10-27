# 2. every_other
# Analizar la complejidad del código
def every_other(array):
    # Suma los elementos de posición par con todos los elementos del arreglo
    for i,e in enumerate(array):# O(n^2) <- n*n 
        if (i % 2 == 0):
            for x in array:# O(n)
                print(e,"+",x,": ",e + x) 
               


arreglo = [1,4,8,2]
every_other(arreglo)
