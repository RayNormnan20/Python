
from random import randint

i = 1

while True:
    edad  = randint(25, 80)
    estado = randint (1, 4)
    if estado == 1:
        estadoCivil = "Soltero"
    elif estado == 2:
        estadoCivil = "Casado"
    elif estado == 3:
        estadoCivil = "Viudo"
    else:
        estadoCivil = "Divorciado"
   
    print("Persona # {}: edad= {}  estado civil= {}" .format(i,edad,estadoCivil))
    
    if edad == 80:
        break
    i += 1

