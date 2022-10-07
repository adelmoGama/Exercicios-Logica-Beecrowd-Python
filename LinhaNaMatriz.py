# import random
L = int(input())
T = input().upper()
matriz = []
qtd_linhas = 12
qtd_colunas = 12
for i in range(qtd_linhas):
    linha = []
    for coluna in range(qtd_colunas):
        valor = float(input())
        linha += [valor]
    matriz += [linha]
print(matriz)
if T == 'S':
    soma = 0
    for coluna in range(qtd_colunas):
        soma += matriz[L][coluna]
    print(soma)
elif T == 'M':
    soma = 0
    for coluna in range(qtd_colunas):
        soma += matriz[L][coluna]
    media = soma / 12
    print("%.1f" % media)
