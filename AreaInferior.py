O = input().upper()
matriz = []
qtd_linhas = 12
qtd_colunas = 12
for l in range(qtd_linhas):
    linha = []
    for c in range(qtd_colunas):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)
soma = 0
inicio = 5
fim = 7
cont = 0
for linha in range(7, 12):
    for coluna in range(inicio, fim):
        soma += matriz[linha][coluna]
        cont += 1
    inicio -= 1
    fim += 1
if O == 'S':
    print("%.1f" % soma)
elif O == 'M':
    media = soma / cont
    print("%.1f" % media)
