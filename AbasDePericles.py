N, M = input().split()
abas = int(N)
for i in range(int(M)):
    acao = input().lower()
    if acao == "fechou":
        abas += 1
    elif acao == "clicou":
        abas -= 1
print(abas)
