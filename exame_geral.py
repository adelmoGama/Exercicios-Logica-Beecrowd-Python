while True:
    try:
        N, Q = input().split()
        notas = []
        for i in range(int(N)):
            n = input()
            notas.append(int(n))
        notas.sort(reverse=True)
        for i in range(int(Q)):
            p = int(input())
            print(notas[p-1])
    except EOFError:
        break
