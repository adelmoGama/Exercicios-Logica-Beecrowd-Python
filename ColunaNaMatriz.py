# import random
C = int(input())
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
    for linha in range(qtd_linhas):
        soma += matriz[linha][C]
    print(soma)
elif T == 'M':
    soma = 0
    for linha in range(qtd_linhas):
        soma += matriz[linha][C]
    media = soma / 12
    print("%.1f" % media)
