T = 1
while T != 0:
    T = int(input())
    for i in range(T):
        N = int(input())
        if N % 2 == 0:
            pedidos = ((N - 2) * 2) + 2
            print(pedidos)
        else:
            pedidos = ((N - 1) * 2) + 1
            print(pedidos)
