# PolishNotation.py

def polishNotation (cadena) :
    # Resuelve las operaciones en notación: polish notation
    stack =[]
    for val in cadena:
        if isNumber(val):
            stack.append(val)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            if val == "+":
                x = a + b
            elif val == "-":
                x = a - b
            elif val == "*":
                x = a * b
            elif val == "/":
                x = int(a / b)
            stack.append(str(x))

    return x

def isNumber(val):
    # Comprueba si el parámetro es número o no
    try:
        int(val)
        return True
    except:
        return False



answer = polishNotation(["2", "1", "+", "3", "*"])
print(answer)
answer = polishNotation(["4", "13", "5", "/", "+"])
print(answer)
answer = polishNotation(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
print(answer)

