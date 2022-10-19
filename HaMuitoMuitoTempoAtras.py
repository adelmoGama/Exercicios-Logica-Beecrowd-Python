N: int = int(input())
for i in range(N):
    T: int = int(input())
    if T > 2015:
        ano = T - 2014
        print(f"{ano} A.C.")
    elif T < 2015:
        ano = 2015 - T
        print(f"{ano} D.C.")
    elif T == 2015:
        print("1 A.C.")
