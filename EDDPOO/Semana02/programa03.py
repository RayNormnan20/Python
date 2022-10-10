while(True):
    try:
        num = float(input("Introduce un número: "))
        num2 = 4
        print("{}/{} = {}".format(num, num2, num/num2))
    except:
        print("Ha ocurrido un error, introduce un número")
    else:
        print ("Todo ha funcionado correctamente")
        break
    finally:
        print("Fin del programa")
