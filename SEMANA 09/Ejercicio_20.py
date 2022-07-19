from random import randint

rango1= 0
rango2= 0
rango3= 0
rango4= 0
rango5= 0

for i in range (75):
    hijos = randint (1,5)
    if hijos == 1:
        rango1 += 1
    elif hijos == 2:
        rango2 += 1
    elif hijos == 3:
        rango3 += 1
    elif hijos == 4:
        rango4 += 1
    else:
        rango5 += 1


print("Un hijo: " + str(rango1))