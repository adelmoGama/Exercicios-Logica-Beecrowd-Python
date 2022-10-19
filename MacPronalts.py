p = int(input())
valor: float = 0
for i in range(p):
    q = input().split(" ")
    id, qtd = q
    id, qtd = int(id), int(qtd)
    if id == 1001:
        valor += qtd * 1.5
    elif id == 1002:
        valor += qtd * 2.5
    elif id == 1003:
        valor += qtd * 3.5
    elif id == 1004:
        valor += qtd * 4.5
    elif id == 1005:
        valor += qtd * 5.5
print("%.2f" % valor)
