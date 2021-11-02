#Q6: Cual es la complejidad de
def sumatoria(n):
    # Acumula la sumatoria de n primeros números
    # La sumatoria no debe ser mayor a n
    p = 0
    for i in range(n):
        p = p + i
        if p > n:
           break
        print(p)
        
sumatoria(10)

# i = 1 | p = 0 + 1
# i = 2 | p = 0 + 1 + 2
# i = 3 | p = 0 + 1 + 2 + 3
# i = k | p = 0 + 1 + 2 ... + k -> k(k+1)/2
# p > n -> k(k+1)/2 > n
# k ^ 2  = n 
# k = n ^ (1/2)
# Complejidad O(n ^ (1/2)) 