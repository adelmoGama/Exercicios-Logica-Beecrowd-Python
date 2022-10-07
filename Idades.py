idade: int = 0
soma: int = 0
cont: int = -1
while True:
    if idade < 0:
        break
    soma += idade
    cont += 1
    idade = int(input())
if cont > 0:
    print(soma)
    print(cont)
    media: float = float(soma / cont)
    print("%.2f" % media)
