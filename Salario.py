# ENTRADAS:
id: int = int(input())
horas: int = int(input())
valorHora: float = float(input())
# PROCESSAMENTO:
salario: float = horas * valorHora
# SAÍDA:
print(f"NUMBER = {id}\nSALARY = U$ %.2f" % salario)
