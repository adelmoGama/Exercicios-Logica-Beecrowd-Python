# DADOS:
pesoA: float = 2.0
pesoB: float = 3.0
pesoC: float = 5.0
# ENTRADAS:
A: float = float(input())
B: float = float(input())
C: float = float(input())
# PROCESSAMENTO:
media: float = ((pesoA * A) + (pesoB * B) + (pesoC * C)) / (pesoA + pesoB + pesoC)
# SAÍDA:
print("MEDIA = %.1f" % media)
