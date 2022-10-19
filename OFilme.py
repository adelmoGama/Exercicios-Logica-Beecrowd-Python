A, B = input().split(" ")
A, B = float(A), float(B)
diferenca: float = B - A
porcentagem: float = (100 * diferenca) / A
print("%.2f" % porcentagem, end="")
print("%")
