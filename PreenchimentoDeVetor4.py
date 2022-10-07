cont: int = 0
par: list = list()
impar: list = list()
contPar: int = 0
contImpar: int = 0
while True:
    if cont >= 15:
        break
    valor: int = int(input())
    if valor % 2 == 0:
        par.append(valor)
        contPar += 1
    elif valor % 2 != 0:
        impar.append(valor)
        contImpar += 1
    if contPar == 5:
        contFor: int = 0
        for pares in par:
            print(f"par[{contFor}] = {pares}")
            contFor += 1
        par.clear()
        contPar = 0
    elif contImpar == 5:
        contFor: int = 0
        for impares in impar:
            print(f"impar[{contFor}] = {impares}")
            contFor += 1
        impar.clear()
        contImpar = 0
    cont += 1

if contImpar > 0:
    contFor: int = 0
    for impares in impar:
        print(f"impar[{contFor}] = {impares}")
        contFor += 1
if contPar > 0:
    contFor: int = 0
    for pares in par:
        print(f"par[{contFor}] = {pares}")
        contFor += 1
