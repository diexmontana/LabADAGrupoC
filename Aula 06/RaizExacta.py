# RaizExacta.py

def raizExacta(val):
    # Comprueba que el valor dado tiene raiz cuadrada exacta
    L = 0
    R = val
    while L <=  R:
        mid = L + (R - L) // 2
        
        cuadrado = mid*mid
        if cuadrado == val:
            return True
        elif cuadrado < val:
            L = mid + 1
        elif cuadrado > val:
            R = mid -1
    return False

print(raizExacta(81))
print(raizExacta(4))
print(raizExacta(20))