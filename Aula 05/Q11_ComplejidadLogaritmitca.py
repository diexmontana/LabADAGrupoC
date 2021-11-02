#Q11: Cual es la complejidad de
def saludo(n):
    p = 0
    i = 1
    for k in range(n):
        i = i * 2
        if i >= n:# Mientras i < n
           break
        p = p + 1
    j = 1
    for k in range(p):
        print("Hola")
        j = j * 2
        if j >= p:# Mientras j < p
           break
        
saludo(10)

# Primer ciclo:
# k = 1 | i = 1 | p = 1
# k = 2 | i = 2 | p = 2
# k = 3 | i = 4 | p = 3
# k = k | i = 2 ^ k | p = k
# i >= n
# 2 ^ k  >= n
# 2 ^ k = n
# k = log en base 2 de n
# p = k
# p = log en base 2 de n

# Segundo ciclo:
# p = log en base 2 de n
# k = 1 | j = 1 
# k = 2 | j = 2 
# k = 3 | j = 4 
# k = k | j = 2 ^ k 
# j >= p
# j >= log en base 2 de n
# 2 ^ k  >= log en base 2 de n
# 2 ^ k = log en base 2 de n
# k = log en base 2 de log en base 2 de n

# Complejidad O(log en base 2 de log en base 2 de n) 