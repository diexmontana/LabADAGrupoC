# UniquePaths2.py

def uniquePaths2(grid):
    # Dada una matriz mxn se requiere el numero de caminos desde la posición (0,0) hasta (m,n)
    # Solo pueden haber movimientos hacia la derecha o hacia abajo
    # Hay obstaculos representados por uno
    
    # Crearemos una matriz donde cada posición indica el número de caminos hasta esa posición
    # Primero llenamos la matriz de ceros
    m = len(grid) # Filas
    n = len(grid[0]) # Columnas
    matriz = [[0 for columna in range(n)] for fila in range(m)]

    mostrarMatriz(matriz)
    # Para todos las posiciones de la 1ra fila el número de caminos es uno
    # Para todos las posiciones de la 1ra columna el número de caminos es uno
    for columna in range(n):
        # Si hay un obstaculo dejamos el resto de elementos de la columna en cero
        if grid[0][columna] == 1:
            break
        matriz[0][columna] = 1
    for fila in range(m):
        # Si hay un obstaculo dejamos el resto de elementos de la fila en cero
        if grid[fila][0] == 1:
            break
        matriz[fila][0] = 1
    mostrarMatriz(matriz)

    # Para las demas posiciones el número de camino se obtiene sumando el valor de arriba y de la izquierda
    for fila in range(1,m):
        for columna in range(1,n):
            # Si hay un obstáculo se hace que esa posición valga cero, para que no incremente la suma
            if grid[fila][columna] == 1:
                matriz[fila][columna] = 0
            else:
                matriz[fila][columna] = matriz[fila - 1][columna] + matriz[fila][columna - 1]
    mostrarMatriz(matriz)
    return matriz[m - 1][n - 1]

def mostrarMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end = "    ")
        print()
    print()

matriz1 = [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]

uniquePaths2(matriz1)