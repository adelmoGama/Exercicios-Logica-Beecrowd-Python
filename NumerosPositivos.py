# CONTADOR:
cont: int = 0
# PROCESSAMENTO:
for numero in range(1, 7):
    # ENTRADA:
    numeros: float = float(input())
    if numeros > 0:
        cont += 1
print(f"{cont} valores positivos")
