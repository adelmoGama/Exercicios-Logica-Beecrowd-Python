N: int = int(input())
cont: int = 1
for i in range(N):
    print(f"{cont ** 1} {cont ** 2} {cont ** 3}")
    print(f"{cont} {(cont ** 2) + 1} {(cont ** 3) + 1}")
    cont += 1
