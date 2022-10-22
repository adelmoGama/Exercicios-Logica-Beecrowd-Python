while True:
    try:
        N, Amin, Amax = input().split()
        qtd = 0
        for i in range(int(N)):
            A = int(input())
            if(A >= int(Amin)) and (A <= int(Amax)):
                qtd += 1
        print(qtd)
    except EOFError:
        break
