N = int(input())
valor = input().split(" ")
menor = 21
posicao = 0
lista = []
for i in valor:
    i = int(i)
    lista.append(i)
for i in range(N):
    if lista[i] < menor:
        menor = lista[i]
        posicao = i
print(posicao+1)
