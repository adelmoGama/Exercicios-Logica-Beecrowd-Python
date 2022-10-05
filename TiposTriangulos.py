# ENTRADA:
A, B, C = input().split(" ")
A: float = float(A)
B: float = float(B)
C: float = float(C)
temporario: int
# PROCESSAMENTO:
if(B > A) and (B > C):
    temporario: float = A
    A = B
    B = temporario
elif C > A:
    temporario: float = A
    A = C
    C = temporario
if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == (B**2 + C**2):
        print("TRIANGULO RETANGULO")
    if A**2 > (B**2 + C**2):
        print("TRIANGULO OBTUSANGULO")
    if A**2 < (B**2 + C**2):
        print("TRIANGULO ACUTANGULO")
    if A == B and A == C:
        print("TRIANGULO EQUILATERO")
    if (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
        print("TRIANGULO ISOSCELES")
