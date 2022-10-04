# DADOS:
pesoA: float = 3.5
pesoB: float = 7.5
# ENTRADAS:
A: float = float(input())
B: float = float(input())
# PROCESSAMENTO:
media: float = ((pesoA * A) + (pesoB * B)) / (pesoA + pesoB)
# SAÍDA:
print("MEDIA = %.5f" % media)
