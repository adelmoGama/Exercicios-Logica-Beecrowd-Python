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
    contM = qtd_colunas
    for linha in range(qtd_linhas):
        contM -= 1
        for coluna in range(contM):
            soma += matriz[linha][coluna]
    print(soma)
elif O == 'M':
    soma = 0
    contM = qtd_colunas
    cont = 0
    for linha in range(qtd_linhas):
        contM -= 1
        for coluna in range(contM):
            soma += matriz[linha][coluna]
            cont += 1
    media = soma / cont
    print("%.1f" % media)
