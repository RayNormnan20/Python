
termino = 6
razon = 2
suma = 0
for i in range (12):
    print(termino, end= " ")
    suma += termino
    termino += razon
    razon *= 2 
    
    

print("\nsuma: "+ str (suma))