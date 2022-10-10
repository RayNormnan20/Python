#Localiza el error en el siguiente bloque de código.
#Crea una excepción para evitar que el programa se bloquee 
#y además explica en un mensaje al usuario la causa y/o solución:

#Ejercicio:

lista = [1, 2, 3, 4, 5]
lista[10]

#Ejecución:

lista = [1, 2, 3, 4, 5]
try:
    lista[10]
except IndexError:
    print("Error:\tEl índice se encuentra fuera del rango,\n"
          "\tdebes utilizar un número mayor o igual que cero\n"
          "\ty menor que la longitud de la lista.")

