while True:
    X: int = int(input())
    if X == 0:
        break
    soma: int = 0
    cont: int = 0
    valor: int = X
    while cont < 5:
        if valor % 2 == 0:
            soma += valor
            cont += 1
            valor += 1
        else:
            valor += 1
    print(soma)
