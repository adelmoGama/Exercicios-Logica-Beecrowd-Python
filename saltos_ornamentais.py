N = int(input())
for i in range(N):
    nome = input()
    GD = float(input())
    notas = []
    N1, N2, N3, N4, N5, N6, N7 = input().split()
    notas.append(float(N1))
    notas.append(float(N2))
    notas.append(float(N3))
    notas.append(float(N4))
    notas.append(float(N5))
    notas.append(float(N6))
    notas.append(float(N7))
    maior = 0
    menor = 10
    for maax in notas:
        if maax > maior:
            maior = maax
    for miin in notas:
        if miin < menor:
            menor = miin
    notas.remove(maior)
    notas.remove(menor)
    soma = 0
    for k in range(int(len(notas))):
        soma += notas[k]
    nota_final = soma * GD
    print(nome, "%.2f" % nota_final)
