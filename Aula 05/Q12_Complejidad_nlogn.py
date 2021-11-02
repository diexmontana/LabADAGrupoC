#Q12: Cual es la complejidad de
def saludo(n):
    j = 1
    for i in range(n):
        for k in range(n):
            print("Hola")
            j = j * 2
            if( j >= n): # mientras j < n
                break

saludo(10)

# Complejidad de ciclo interno
# k = 1 | j = 1 * 2
# k = 2 | j = 1 * 2 * 2
# k = 3 | j = 1 * 2 * 2 * 2
# k = k | j = 2 ^ k
# j >= n
# 2 ^ k >= n
# 2 ^ k  = n 
# k = log base 2 de n
# Complejidad O(log base 2 de n) 

# Complejidad de ciclo externo
# n * log base 2 de n
# Complejidad O(n * log base 2 de n)