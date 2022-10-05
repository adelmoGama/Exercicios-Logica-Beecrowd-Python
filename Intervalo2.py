inn: int = 0
out: int = 0
N: int = int(input())
for i in range(1, N+1):
    X: int = int(input())
    if (X >= 10) and (X <= 20):
        inn += 1
    else:
        out += 1
print(f"{inn} in")
print(f"{out} out")
