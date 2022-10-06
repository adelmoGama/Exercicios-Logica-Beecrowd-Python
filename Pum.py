N: int = int(input())
cont: int = 0
inicio: int = 1
while True:
    if cont >= N:
        break
    for i in range(inicio, inicio+3):
        print(i, end=" ")
    print("PUM")
    inicio += 4
    cont += 1
