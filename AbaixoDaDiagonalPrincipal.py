# import random
O = input().upper()
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
if O == 'S':
    soma = 0
    for linha in range(qtd_linhas):
        for coluna in range(qtd_colunas):
            if linha > coluna:
                soma += matriz[linha][coluna]
elif O == 'M':
    soma = 0
    cont = 0
    for linha in range(qtd_linhas):
        for coluna in range(qtd_colunas):
            if linha > coluna:
                soma += matriz[linha][coluna]
                cont += 1
    media = soma / cont
    print("%.1f" % media)
