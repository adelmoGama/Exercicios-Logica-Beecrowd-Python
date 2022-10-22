N: int = int(input())
L = input().split()
lista = []
for i in L:
    lista.append(int(i))
mult2 = 0
mult3 = 0
mult4 = 0
mult5 = 0
for i in lista:
    if i % 2 == 0:
        mult2 += 1
    if i % 3 == 0:
        mult3 += 1
    if i % 4 == 0:
        mult4 += 1
    if i % 5 == 0:
        mult5 += 1
print(f"{mult2} Multiplo(s) de 2")
print(f"{mult3} Multiplo(s) de 3")
print(f"{mult4} Multiplo(s) de 4")
print(f"{mult5} Multiplo(s) de 5")
