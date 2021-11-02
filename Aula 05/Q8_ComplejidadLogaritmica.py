#Q8: Cual es la complejidad de
def DividirEntreDos(n):
    # Divide entre mientras el resultado sea mayor que uno
    p = n
    for i in range(n):
        print(p)
        p = p / 2
        if p < 1:
           break
        
DividirEntreDos(10)

# i = 1 | p = n / 2
# i = 2 | p = n / 2 / 2
# i = 3 | p = n / 2 / 2 / 2
# i = k | p = n / ( 2 ^ k)
# p < 1
# n / (2 ^ k)  < 1
# n < 2 ^ k 
# n = 2 ^ k 
# k = log base 2 de n
# Complejidad O(log base 2 de n) 