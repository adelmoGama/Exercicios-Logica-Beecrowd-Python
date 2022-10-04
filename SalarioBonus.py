# ENTRADAS:
nome: str = input()
salarioFixo: float = float(input())
vendas: float = float(input())
# PROCESSAMENTO:
salario: float = salarioFixo + (0.15 * vendas)
# SAÍDA:
print("TOTAL = R$ %.2f" % salario)
