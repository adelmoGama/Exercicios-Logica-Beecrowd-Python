QT: int = int(input())
for i in range(QT):
    nome1, escolha1, nome2, escolha2 = input().split(" ")
    escolha1, escolha2 = str(escolha1).upper(), str(escolha2).upper()
    N, M = input().split(" ")
    N, M = int(N), int(M)
    if escolha1 == "PAR":
        if(N + M) % 2 == 0:
            print(nome1)
        else:
            print(nome2)
    elif escolha1 == "IMPAR":
        if(N + M) % 2 != 0:
            print(nome1)
        else:
            print(nome2)
