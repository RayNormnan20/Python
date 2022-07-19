

def suma (a,b):
    return a + b

def resta (a,b):
    return a - b

def producto (a,b):
    return a * b

def division (a,b):
    if b!= 0:
        return a / b
    else:
        return"La divión no se puede realizar"

x= 10
y = 6

print("La suma es:",suma (x,y))
print("La resta es:",resta (x,y))
print("El producto es:",producto (x,y))
print("La división es:",division(x,y))
