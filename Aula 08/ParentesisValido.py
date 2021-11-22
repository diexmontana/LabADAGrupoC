#ParentesisValido.py

def parentesisValido (cadena) :
    # Comprueba los pares de parentesis validos que abren y cierran
    # Devuelve el numero de parentesis sobrantes
    stack =[]

    for val in cadena:
        if val == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop(-1)
            else:
                stack.append(val)
        else:
            stack.append(val)

    return len(stack)

print(parentesisValido("())"))
print(parentesisValido("((("))
print(parentesisValido("(()))("))
print(parentesisValido("()))(("))

