X, M = input().split()
while True:
    X, M = int(X), int(M)
    E = X * M
    print(E)
    X, M = input().split()
    if X == M == "0":
        break
