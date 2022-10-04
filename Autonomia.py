# DADOS:
autonomiaFixa: float = 12
# ENTRADAS:
tempo: int = int(input())
velocidade: int = int(input())
# PROCESSAMENTO:
distancia: float = float(velocidade * tempo)
autonomia: float = float(distancia / autonomiaFixa)
# SAÍDA:
print("%.3f" % autonomia)
