# InterviewWait.py

from collections import deque

def tiempoEspera(turnos):
    # Recibe una lista de numeros que representan el tiempo de cada turno
    # El turno del usuario se representa con -1
    # Devuelve el timpo que pasa antes de que atiendan al usuario
    tiempo = 0
    queue = deque(turnos)
    a = queue[0]
    b = queue[-1]
    while a != -1 and b != -1:
        if a < b:
            tiempo = tiempo + queue.popleft()
        else:
            tiempo = tiempo + queue.pop()
        a = queue[0]
        b = queue[-1]
    return tiempo

print(tiempoEspera([4, -1, 5, 2, 3]))