# Dyslectionary.py
def dislectionary(palabras):
    lista = []
    maxLongitud = 0
    for pal in  palabras:
        longitud = len(pal)
        if maxLongitud < longitud:
            maxLongitud = longitud
        lista.append(pal[len(pal)::-1])
    lista.sort()

    lista2 = []
    
    for pal in  lista:
        longitud = len(pal)
        espacios = maxLongitud - longitud 
        lista2.append(" "*espacios + pal[len(pal)::-1])

    for pal in  lista2:
        if pal == " ":
            print()
        else:
            print(pal)

    #return(lista2)


palabras = ["apple","banana","grape","kiwi","pear", " ", "airplane","bicycle","boat","car"]
print(dislectionary(palabras))
