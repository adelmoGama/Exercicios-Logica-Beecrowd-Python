T: int = int(input())
N: list = list()
cont: int = 0
while True:
    if cont > 999:
        break
    for i in range(0, T):
        if cont > 999:
            break
        N.append(i)
        cont += 1
cont: int = 0
for i in N:
    print(f"N[{cont}] = {N[i]}")
    cont += 1
