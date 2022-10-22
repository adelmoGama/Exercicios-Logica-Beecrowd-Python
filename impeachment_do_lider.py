while True:
    try:
        N = int(input())
        v = input().split()
        sim = 0
        nao = 0
        for i in v:
            if int(i) == 1:
                sim += 1
            elif int(i) == 0:
                nao += 1
        if sim >= ((2/3)*N):
            print("impeachment")
        else:
            print("acusacao arquivada")
    except EOFError:
        break
