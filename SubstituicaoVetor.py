X = list(range(10))
for i in range(len(X)):
    X[i] = int(input())
for i in range(len(X)):
    if X[i] < 1:
        X[i] = 1
for i in range(len(X)):
    print(f"X[{i}] = {X[i]}")
