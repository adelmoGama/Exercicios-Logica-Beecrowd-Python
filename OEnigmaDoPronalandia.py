n = int(input())
n = list(str(n))
qtd = int(len(n))
inversa = n.reverse()
for i in range(qtd):
    if i == (qtd-1):
        print(n[i])
    else:
        print(n[i], end="")
