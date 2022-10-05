# ENTRADAS:
A, B, C = input().split(" ")
A: float = float(A)
B: float = float(B)
C: float = float(C)
maior: float
soma: float
true: bool
# PROCESSAMENTO:
if(A > B) and (A > C):
    maior = A
elif B > C:
    maior = B
else:
    maior = C
if maior == A:
    soma = B + C
elif maior == B:
    soma = A + C
else:
    soma = A + B
if soma > maior:
    true = True
else:
    true = False
if true:
    perimetro: float = A + B +C
    print("Perimetro = %.1f" % perimetro)
else:
    area: float = ((A + B) * C) / 2
    print("Area = %.1f" % area)
