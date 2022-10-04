# ENTRADA:
A, B, C = input().split(" ")
A: int = int(A)
B: int = int(B)
C: int = int(C)
maior: int
# PROCESSAMENTO:
maiorP: int = int((A + B + abs(A - B))/2)
maior: int = int((maiorP + C + abs(maiorP - C)) / 2)
print(f"{maior} eh o maior")
