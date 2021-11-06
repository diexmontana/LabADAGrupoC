# MenorRotado.py

def menorRotado(arr):
    # Encuentra el menor elemento en un arreglo ordenado rotado
    L = 0
    R = len(arr) - 1
    menor = 0
    while L <=  R:
        mid = L + (R - L) // 2
        if mid == L  or mid == R:
            if arr[L] < arr[R]:
                return arr[L]
            else:
                return arr[R]
        elif arr[mid] > arr[R]:
            L = mid
        elif arr[mid] < arr[R]:
            R = mid
    return arr[menor]

arreglo01 = [6, 7, 9, 15, 19, 2, 3]
arreglo02 = [7, 9, 15, 19, 2, 3, 6]
arreglo03 = [9, 15, 19, 2, 3, 6, 7]
arreglo04 = [15, 19, 2, 3, 6, 7, 9]
arreglo05 = [19, 2, 3, 6, 7, 9, 15]
arreglo06 = [2, 3, 6, 7, 9, 15, 19]

print(menorRotado(arreglo01))
print(menorRotado(arreglo02))
print(menorRotado(arreglo03))
print(menorRotado(arreglo04))
print(menorRotado(arreglo05))
print(menorRotado(arreglo06))