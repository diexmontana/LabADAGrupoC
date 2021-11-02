#Q10: Cual es la complejidad de
def imprimir(n):
    # Imprime los n primeros números 2 veces
    for i in range(n): # O(n)
        print(i)
    for j in range(n): # O(n)
        print(j)

imprimir(10)

# O(n) + O(n)
# Complejidad O(n)