while True:
    nota1: float = float(input())
    if(nota1 >= 0) and (nota1 <= 10):
        break
    print("nota invalida")
while True:
    nota2: float = float(input())
    if(nota2 >= 0) and (nota2 <= 10):
        break
    print("nota invalida")
media: float = float((nota1 + nota2) / 2)
print("media = %.2f" % media)
