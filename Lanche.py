# ENTRADA:
id, quantidade = input().split(" ")
if int(id) == 1:
    valor = float(4.00 * int(quantidade))
    print("Total: R$ %.2f" % valor)
elif int(id) == 2:
    valor = float(4.50 * int(quantidade))
    print("Total: R$ %.2f" % valor)
elif int(id) == 3:
    valor = float(5.00 * int(quantidade))
    print("Total: R$ %.2f" % valor)
elif int(id) == 4:
    valor = float(2.00 * int(quantidade))
    print("Total: R$ %.2f" % valor)
elif int(id) == 5:
    valor = float(1.50 * int(quantidade))
    print("Total: R$ %.2f" % valor)
