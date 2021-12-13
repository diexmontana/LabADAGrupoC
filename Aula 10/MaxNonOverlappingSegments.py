# MaxNonOverlappingSegments.py

def maxNonOverlappingSegments(listA, listB):
    # Devuelve el número máximo de segmentos que no se sobreponen
    
    segments = len(listA)
    extremo = listB[0]# Representa el extremo del primer segmento
    for i in range(1, len(listA)):
        # Para saber si no se sobreponen comparamos el extremo del primer segmento
        # con el inicio del siguiente 
        if listA[i] > extremo:
            extremo = listB[i]
        else:
            # Si se sobreponen, descontamos en uno al numero de segmentos
            # Cuando dos segmentos se sobreponen escogemos aquel segmento
            # cuyo extremo es numero menor, para que haya menor numero de sobreposiciones en los 
            # siguientesciclos
            segments -= 1
            extremo = min(listB[i], extremo)
    return segments

A = [1,3,7,9,9]
B = [5,6,8,9,10]

print(maxNonOverlappingSegments(A, B))
