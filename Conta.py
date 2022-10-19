C: int = int(input())
for i in range(C):
    N: int = int(input())
    inteiro: int = 1
    soma: int = 0
    for k in range(N):
        soma += inteiro
        inteiro *= -1
    print(soma)
