# ENTRADA:
N: int = int(input())
# AUXILIAR:
aux: int
# PROCESSAMENTO:
horas: int = int(N / 3600)
aux: int = N - int(horas * 3600)
minutos: int = int(aux / 60)
aux: int = aux - int(minutos * 60)
segundos: int = aux
# SAÍDA:
print(f"{horas}:{minutos}:{segundos}")
