#El procesamiento será extremadamente fácil: 
# queremos que los números se sumen.

line = input("Introduzca números separados con espacios: ")
strings = line.split()
sum = 0
try:
    for substr in strings:
        sum += float(substr)
    print("Sum = ", sum)
except:
    print("No es un número: ", substr)
finally:
    print("Programa finalizado")
