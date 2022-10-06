maior: int = 0
posicao: int = 0
valor: int = 0
for i in range(3):
    valor = int(input())
    if valor > maior:
        maior = valor
        posicao = i+1
print(f"{maior}\n{posicao}")
