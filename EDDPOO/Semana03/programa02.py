#Cada letra corre una hacia atras 

cipher = input("Ingresar en el criptograma: ")
text = ""
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord("A"):
        code = ord("Z")
    text += chr(code)
print(text)



