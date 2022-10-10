iban = input("Entrar IBAN, por favor: ")
iban = iban.replace(' ','')
if not iban.isalnum():
    print("Caracteres inválidos dentro de IBAN - lo siento!")
elif len(iban) < 15:
    print("IBAN demasiado corto")
elif len(iban) > 31:
    print("IBAN demasiado largo")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ""
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord("A"))
    ibann = int(iban2)
    if ibann % 97 == 1:
        print("¡Parece legítimo!")
    else:
        print("No creo que sea un IBAN válido, lo siento")

