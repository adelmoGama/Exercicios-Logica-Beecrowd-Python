A = []
for i in range(100):
    x: float = float(input())
    A.append(x)
    if x <= 10.0:
        print(f"A[{i}] = {x}")
