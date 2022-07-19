def NumEnteroPositivo (num):
    if len(str(num)) >= 3 and num > 0:
        d = len (str(num))
        D = 10** (int(d)-1)
        return(num % D) // 10
    else:
        return "El número no es valido"
num = 99221
salida = NumEnteroPositivo (num)
print(salida)
