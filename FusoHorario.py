S, T, F = input().split(" ")
S, T, F = int(S), int(T), int(F)
soma = S + T + F
if soma > 23:
    hora = soma - 24
    print(hora)
elif soma < 0:
    hora = 24 + soma
    print(hora)
else:
    print(soma)
