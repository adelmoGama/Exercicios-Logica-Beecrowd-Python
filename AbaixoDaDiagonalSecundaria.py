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
if O == 'S':
    soma = 0
    for linha in range(1, qtd_linhas):
        for coluna in range(qtd_colunas-linha, qtd_colunas):
            soma += matriz[linha][coluna]
    print(soma)
elif O == 'M':
    soma = 0
    cont = 0
    for linha in range(1, qtd_linhas):
        for coluna in range(qtd_colunas-linha, qtd_colunas):
            soma += matriz[linha][coluna]
            cont += 1
    media = soma / cont
    print("%.1f" % media)
