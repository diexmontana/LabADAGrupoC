# BinarySearch.py

def binarySearch(arr, target):
    # Devuelve la posicion del elemento dado en el arreglo
    # Si no lo encuentra devuelve -1
    L = 0
    R = len(arr) - 1
    while L <=  R:
        mid = L + (R - L) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            L = mid + 1
        elif arr[mid] > target:
            R = mid -1
    return -1

arreglo = [2,4,8,9,10,22,25,26,28,29,30,42,45,56]

print(binarySearch(arreglo,22))
print(binarySearch(arreglo,24))