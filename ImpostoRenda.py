# ENTRADA:
salario: float = float(input())
# PROCESSAMENTO:
if (salario >= 0) and (salario <= 2000):
    print("Isento")
elif(salario > 2000) and (salario <= 3000):
    imposto: float = (salario - 2000) * 0.08
    print("R$ %.2f" % imposto)
elif(salario > 3000) and (salario <= 4500):
    imposto: float = 80 + ((salario - 3000) * 0.18)
    print("R$ %.2f" % imposto)
elif salario > 4500:
    imposto: float = 350 + ((salario - 4500) * 0.28)
    print("R$ %.2f" % imposto)
