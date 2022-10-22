while True:
    try:
        N, I = input().split()
        id = []
        jogo = []
        for k in range(int(N)):
            i, j = input().split()
            id.append(int(i))
            jogo.append(int(j))
        indice = []
        for a in range(int(len(id))):
            if int(id[a]) == int(I):
                indice.append(a)
        meus = 0
        for a in indice:
            if jogo[a] == 0:
                meus += 1
        print(meus)
    except EOFError:
        break
