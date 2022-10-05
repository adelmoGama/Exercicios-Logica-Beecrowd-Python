
cont: int = 0
valor: int = int(input())
while cont < 6:
    if valor % 2 != 0:
        print(valor)
        cont += 1
    valor += 1
