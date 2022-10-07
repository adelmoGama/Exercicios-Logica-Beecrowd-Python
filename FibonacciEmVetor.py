T = int(input())
for i in range(T):
    N = int(input())
    fibonacci = [0, 1]
    for k in range(1, N):
        valor = (fibonacci[k]) + (fibonacci[k-1])
        fibonacci.append(valor)
    print(f"Fib({N}) = {fibonacci[N]}")
