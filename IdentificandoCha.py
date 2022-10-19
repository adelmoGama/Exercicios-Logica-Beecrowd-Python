T = input()
respostas = input().split(" ")
soma = 0
for resposta in respostas:
    if resposta == T:
        soma += 1
print(soma)
