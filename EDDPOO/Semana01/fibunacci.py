def fibunacci (n):
    resultado = []
    num1, num2 = 0, 1
    while num2 < n:
        resultado.append(num2)
        num1, num2 = num2, num1 + num2
    return resultado
