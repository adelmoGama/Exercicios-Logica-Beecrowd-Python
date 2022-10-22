N = int(input())
S_total = 0
B_total = 0
A_total = 0
S_efetivo = 0
B_efetivo = 0
A_efetivo = 0
for i in range(N):
    nome = input()
    S, B, A = input().split()
    S_total += int(S)
    B_total += int(B)
    A_total += int(A)
    S1, B1, A1 = input().split()
    S_efetivo += int(S1)
    B_efetivo += int(B1)
    A_efetivo += int(A1)
s = 100*(S_efetivo/S_total)
b = 100*(B_efetivo/B_total)
a = 100*(A_efetivo/A_total)
print("Pontos de Saque: %.2f" % s, end=" ")
print("%.")
print("Pontos de Bloqueio: %.2f" % b, end=" ")
print("%.")
print("Pontos de Ataque: %.2f" % a, end=" ")
print("%.")
