while True:
    valores = input().split()
    A = int(valores[0])
    N = int(valores[-1])
    soma = 0
    for i in range(N):
        soma += (A + i)
    print(soma)
    break
