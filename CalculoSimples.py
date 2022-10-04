# ENTRADAS:
dados1 = input().split(" ")
dados2 = input().split(" ")
# PROCESSAMENTO:
id1, quantidade1, valor1 = dados1
id2, quantidade2, valor2 = dados2
valorFinal: float = (int(quantidade1) * float(valor1)) + (int(quantidade2) * float(valor2))
# SAÍDA:
print("VALOR A PAGAR: R$ %.2f" % valorFinal)
