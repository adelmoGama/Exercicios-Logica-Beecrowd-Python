cont: int = 0
for i in range(1, 6):
    numero: int = int(input())
    if numero % 2 == 0:
        cont += 1
print(f"{cont} valores pares")
