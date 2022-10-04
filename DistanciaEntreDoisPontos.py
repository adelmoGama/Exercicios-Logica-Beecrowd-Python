# DADOS:
dados1 = input().split(" ")
dados2 = input().split(" ")
x1, y1 = dados1
x2, y2 = dados2
# PROCESSAMENTO:
distancia: float = (((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2)) ** (1/2)
# SAÍDA:
print("%.4f" % distancia)
