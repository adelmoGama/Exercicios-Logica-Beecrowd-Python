n = int(input())
matricula = []
notas = []
for i in range(n):
    m, nota = input().split(" ")
    m, nota = int(m), float(nota)
    matricula.append(m)
    notas.append(nota)
notaP = 0.0
parametro = 0
for k in range(n):
    if float(notas[k]) > float(notaP):
        notaP = notas[k]
        parametro = k
if int(notaP) >= 8:
    print(matricula[parametro])
else:
    print("Minimum note not reached")
