while(True):
    try: #Bucle obligatorio
        num = float(input("Introduce un número: "))
        num2 = 4
        print("{}/{} = {}".format(num, num2, num/num2))
    except: #Bucle obligatorio
        print("Ha ocurrido un error, introduce un número")
    else:  #Bucle opcional
        print ("Todo ha funcionado correctamente")
        break
    finally: #Bucle opcional
        print("Fin del programa")