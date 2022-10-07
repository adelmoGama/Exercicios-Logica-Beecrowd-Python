N: int = int(input())
valores = input().split(" ")
for i in range(len(valores)):
    k = int(valores[i])
menor = min(valores)
posicao: int = 0
for i in range(len(valores)):
    if valores[i] == menor:
        posicao += i
print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")
