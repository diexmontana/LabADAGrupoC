# ColorearAreaLimitada.py

def colorearArea(matriz, x, y):
    # Colorea un area de ceros limitada por #
    # depth first search
    matriz[x][y] = 3
    vecinos = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for i, j in vecinos:
        if i >= 0 and j >= 0 and i < len(matriz) and j < len(matriz[0]) and matriz[i][j] == "0":
            colorearArea(matriz, i, j)
    return matriz

def mostrarMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end = " ")
        print()

matriz =[["#", "#", "#", "#", "#", "#"],
        ["#", "0", "0", "0", "0", "#"],
        ["#", "0", "0", "0", "0", "#"],
        ["#", "0", "0", "0", "0", "#"],
        ["#", "0", "0", "0", "#", "0"],
        ["#", "#", "#", "#", "0", "0"]]

mostrarMatriz(colorearArea(matriz,2,2))
print()

matriz =[["#", "#", "#", "#", "#", "#"],
        ["#", "0", "0", "0", "0", "#"],
        ["#", "0", "0", "0", "0", "#"],
        ["#", "0", "0", "0", "0", "#"],
        ["#", "0", "0", "0", "#", "0"],
        ["#", "#", "#", "#", "0", "0"]]

mostrarMatriz(colorearArea(matriz,5,5))