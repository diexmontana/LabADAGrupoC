#AreaMaxima.py

def areaMaxima( matriz):
    # halla la isla de mayor tamaño
    # la isla esta formada por los numero uno contiguos
    area = 0
    for x in range(len(matriz)):
        for y in range(len(matriz[0])):
            if matriz[x][y] == 1:
                area = max(area,dfs(matriz, x, y))
    return area

def dfs(matriz, x, y):
    # depth first search
        matriz[x][y] = 0
        area = 1
        vecinos = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for i, j in vecinos:
            if i >= 0 and j >= 0 and i < len(matriz) and j < len(matriz[0]) and matriz[i][j] == 1:
                area += dfs(matriz, i, j)
        return area
    
    



matriz = grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(areaMaxima(matriz))