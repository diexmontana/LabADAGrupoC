# MayorIgual.py

def mayorIgual(arr, x):
    # Encuentra el primer valor mayor o igual que x
    L = 0
    R = len(arr) - 1
    mayor_igual = 0
    while L <=  R:
        mid = L + (R - L) // 2
        if arr[mid] == x:
            mayor_igual = mid
            return arr[mayor_igual] 
        elif arr[mid] < x:
            L = mid + 1
        elif arr[mid] > x:
            mayor_igual = mid
            R = mid -1
    return arr[mayor_igual]

arreglo = [2,4,8,9,10,22,25,26,28,29,30,42,45,56]

print(mayorIgual(arreglo,30))
print(mayorIgual(arreglo,40))