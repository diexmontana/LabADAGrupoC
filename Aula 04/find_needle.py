# 4. find_needle
# Analizar la complejidad del código:
def fin_needle(needle, haystack): # O(n^2)
    # Encuentra si el prime parámetro string esta contenido en el segundo
    needle_index = 0
    haystack_index = 0
    found_needle = False

    while haystack_index < len(haystack): # O(n^2) <- n*n 
        if needle[needle_index] == haystack[haystack_index]:
            found_needle = True
            while needle_index < len(needle): # O(n)
                if needle[needle_index] != haystack[haystack_index + needle_index]:
                    found_needle = False
                    break
                needle_index += 1
            if found_needle:
                return True
        needle_index = 0
        haystack_index += 1
    return False

print(fin_needle("fgh","abcdefgh"))



