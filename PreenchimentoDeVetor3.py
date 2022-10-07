X: float = float(input())
N: list = list()
cont: int = 1
for i in range(100):
    if i == 0:
        N.append(X/cont)
        cont += 1
    else:
        valor: float = (X / 2)
        N.append(valor)
        X = X / 2
    print(f"N[{i}] = %.4f" % N[i])
