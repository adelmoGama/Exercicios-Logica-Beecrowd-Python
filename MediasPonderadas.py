N: int = int(input())
for i in range(N):
    v1, v2, v3 = input().split(" ")
    v1: float = float(v1)
    v2: float = float(v2)
    v3: float = float(v3)
    media: float = float(((v1 * 2) + (v2 * 3) + (v3 * 5)) / 10)
    print("%.1f" % media)
