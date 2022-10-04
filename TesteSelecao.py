# ENTRADA:
dados = input().split(" ")
A, B, C, D = dados
# PROCESSAMENTO:
if int(B) > int(C) and int(D) > int(A) and int(C+D) > int(A+B) and int(C) > 0 and int(D) > 0 and int(A) % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
