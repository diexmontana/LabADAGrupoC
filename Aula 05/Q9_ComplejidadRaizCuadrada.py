#Q9: Cual es la complejidad de
def cuadrado(n):
    # Eleva al cuadrado los n primero números mientras el resultado sea menor que n
    p = 0
    for i in range(n):
        p = i * i
        if p >= n:
           break
        print(p)
cuadrado(10)

# i = 1 | p = 1 * 1
# i = 2 | p = 2 * 2
# i = 3 | p = 3 * 3
# i = k | p = k * k = k ^ 2
# p >= n
# k ^ 2  >= n
# k ^ 2 = n
# k = n ^ (1/2)
# Complejidad O(n ^ (1/2)) 