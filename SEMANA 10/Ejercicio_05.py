suma = 0
for n in range(0, 15):
    suma += (5 * n + 1) / (4 * n + 1)
    print(f"{5 * n + 1}/{4 * n + 1}", end=",")
print()
print(f"La suma es {suma:.3f}")