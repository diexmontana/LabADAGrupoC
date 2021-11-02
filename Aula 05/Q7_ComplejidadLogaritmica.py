#Q7: Cual es la complejidad de
def potenciaDos(n):
    # Acumula la multiplicacion por 2 de los n primeros números
    # La sumatoria no debe ser mayor a n
    p = 1
    for i in range(n):
        print(p)
        p = p * 2
        if p >= n:
           break
        
potenciaDos(10)

# i = 1 | p = 1 * 2
# i = 2 | p = 1 * 2 * 2
# i = 3 | p = 1 * 2 * 2 * 2
# i = k | p = 2 ^ k
# p >= n -> 2 ^ k >= n
# 2 ^ k  = n 
# k = log base 2 de n
# Complejidad O(log base 2 de n) 