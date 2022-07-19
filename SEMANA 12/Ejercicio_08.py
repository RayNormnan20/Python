#Un año es bisiesto si es múltiplo de 4 pero no múltiplo de 100,
 #aunque los múltiplos de 400 sí lo son. }


def esBisiesto (año):
    if año % 400 == 0:
        return True
    elif año % 100 == 0:
        return False
    elif año % 4 == 0:
        return True
    else:
        return False
        

print(2012,esBisiesto(2012))
print(2010,esBisiesto(2010))
print(2000,esBisiesto(2000))
print(1900,esBisiesto(1900))