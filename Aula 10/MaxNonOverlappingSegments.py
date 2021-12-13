# MaxNonOverlappingSegments.py

def maxNonOverlappingSegments(listA, listB):
    segments = len(listA)
    extremo = listB[0]
    for i in range(1, len(listA)):
        if listA[i] > extremo:
            extremo = listB[i]
        else:
            segments -= 1
            extremo = min(listB[i], extremo)
    return segments

A = [1,3,7,9,9]
B = [5,6,8,9,10]

print(maxNonOverlappingSegments(A, B))