text = input("Ingrese el mensaje que desea cifrar : ")
cipher = ""
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord("Z"):
        code = ord("A")
    cipher += chr(code)
print(cipher)


