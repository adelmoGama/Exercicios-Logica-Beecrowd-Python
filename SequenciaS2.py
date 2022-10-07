soma: float = 1
cont: int = 3
dev: int = 2
for i in range(0, 20):
    s = cont / dev
    soma += s
    cont += 2
    dev *= 2
print("%.2f" % soma)
