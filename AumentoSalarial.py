# ENTRADA:
salario: float = float(input())
# PROCESSAMENTO:
if(salario >= 0) and (salario <= 400):
    salarioR = salario + (0.15 * salario)
    reajuste = 0.15 * salario
    print("Novo salario: %.2f" % salarioR)
    print("Reajuste ganho: %.2f" % reajuste)
    print("Em percentual: 15 %")
elif(salario > 400) and (salario <= 800):
    salarioR = salario + (0.12 * salario)
    reajuste = 0.12 * salario
    print("Novo salario: %.2f" % salarioR)
    print("Reajuste ganho: %.2f" % reajuste)
    print("Em percentual: 12 %")
elif(salario > 800) and (salario <= 1200):
    salarioR = salario + (0.10 * salario)
    reajuste = 0.10 * salario
    print("Novo salario: %.2f" % salarioR)
    print("Reajuste ganho: %.2f" % reajuste)
    print("Em percentual: 10 %")
elif(salario > 1200) and (salario <= 2000):
    salarioR = salario + (0.07 * salario)
    reajuste = 0.07 * salario
    print("Novo salario: %.2f" % salarioR)
    print("Reajuste ganho: %.2f" % reajuste)
    print("Em percentual: 7 %")
elif salario > 2000:
    salarioR = salario + (0.04 * salario)
    reajuste = 0.04 * salario
    print("Novo salario: %.2f" % salarioR)
    print("Reajuste ganho: %.2f" % reajuste)
    print("Em percentual: 4 %")
