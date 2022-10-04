# ENTRADA:
dados = input().split(" ")
A, B, C = dados
# PROCESSAMENTO:
delta: float = float(B) ** 2 - (4 * float(A) * float(C))
if float(A) == 0 or delta < 0:
    print("Impossivel calcular")
else:
    raiz: float = delta ** (1 / 2)
    x1: float = (-float(B) + raiz) / (2 * float(A))
    x2: float = (-float(B) - raiz) / (2 * float(A))
# SAÍDA:
    print("R1 = %.5f" % x1)
    print("R2 = %.5f" % x2)
