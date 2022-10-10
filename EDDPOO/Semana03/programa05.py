#Introducir un texto e indicar cuantas palabras tiene y cuáles son:


# Introducir un texto
Texto = input("Introducir texto: ")

# Convertir un texto a una lista de palabras
Palabra_cadenas = Texto.split()

# Visualizar para las palabras del texto introducido
print("Listado de palabras")
for i, Listado_palabra in enumerate(Palabra_cadenas):
    print("La palabra: ", Listado_palabra)

# Visualizar el número de palabras introducidas
print("El texto tiene: ", i + 1, "palabras")
