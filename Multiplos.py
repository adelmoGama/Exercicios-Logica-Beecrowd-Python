# ENTRADA:
A, B = input().split(" ")
A: int = int(A)
B: int = int(B)
# PROCESSAMENTO:
if A % B == 0 or B % A == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
