M, N = input().split(" ")
M: int = int(M)
N: int = int(N)
soma: int = 0
while True:
    if(M <= 0) or (N <= 0):
        break
    if M < N:
        for i in range(M, N+1):
            soma += i
            print(i, end=" ")
        print(f"Sum={soma}")
    elif N < M:
        for i in range(N, M+1):
            soma += i
            print(i, end=" ")
        print(f"Sum={soma}")
    M, N = input().split(" ")
    M: int = int(M)
    N: int = int(N)
    soma = 0
