while True:
    try:
        N = int(input())
        qtd = 0
        valor = N
        while True:
            if valor == 1:
                break
            valor -= (valor/2)
            qtd += 1
        print(qtd)
    except EOFError:
        break
