# ENTRADA:
N: int = int(input())
# AUXILIAR:
atualizado: int = N
# PROCESSAMENTO:
nota100: int = int(atualizado / 100)
atualizado: int = (N - (nota100 * 100))
nota50: int = int(atualizado / 50)
atualizado: int = atualizado - (nota50 * 50)
nota20: int = int(atualizado / 20)
atualizado: int = atualizado - (nota20 * 20)
nota10: int = int(atualizado / 10)
atualizado: int = atualizado - (nota10 * 10)
nota5: int = int(atualizado / 5)
atualizado: int = atualizado - (nota5 * 5)
nota2: int = int(atualizado / 2)
atualizado: int = atualizado - (nota2 * 2)
nota1: int = atualizado
# SAÍDA:
print(f"{N}")
print(f"{nota100} nota(s) de R$ 100,00")
print(f"{nota50} nota(s) de R$ 50,00")
print(f"{nota20} nota(s) de R$ 20,00")
print(f"{nota10} nota(s) de R$ 10,00")
print(f"{nota5} nota(s) de R$ 5,00")
print(f"{nota2} nota(s) de R$ 2,00")
print(f"{nota1} nota(s) de R$ 1,00")
