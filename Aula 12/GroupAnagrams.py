# GroupAngrams.py
def groupAnagrams(strs):
    
    diccionario = {}
    for pal in strs:
        palOrdenada = sorted(pal)
        palOrdenada = "".join(palOrdenada)
        print(palOrdenada)

        if palOrdenada not in diccionario:
            diccionario[palOrdenada] = [pal]
        else:
            diccionario[palOrdenada].append(pal)
    matriz = []
    for i in diccionario.values():
        matriz.append(i)
   
    return matriz

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)