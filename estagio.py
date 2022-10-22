while True:
    try:
        M = int(input())
        soma = 0
        carga = 0
        for i in range(M):
            N, C = input().split()
            soma += (int(N) * int(C))
            carga += int(C)
        IRA = soma / (carga * 100)
        print("%.4f" % IRA)
    except EOFError:
        break
