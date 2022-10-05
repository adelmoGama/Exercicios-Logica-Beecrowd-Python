cont: int = 0
soma: float = 0

for numero in range(1, 7):
    valor: float = float(input())
    if valor > 0:
        cont += 1
        soma += valor
print(f"{cont} valores positivos")
media: float = float(soma / cont)
print("%.1f" % media)
