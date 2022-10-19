p, j1, j2, r, a = input().split(" ")
p = int(p)
j1 = int(j1)
j2 = int(j2)
r = int(r)
a = int(a)
if p == 1:
    if(r == 0) and (a == 0):
        soma = j1 + j2
        if soma % 2 == 0:
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")
    elif(r == 1) and (a == 1):
        print("Jogador 2 ganha!")
    elif(r == 1) and (a == 0):
        print("Jogador 1 ganha!")
    elif(r == 0) and (a == 1):
        print("Jogador 1 ganha!")
else:
    if(r == 0) and (a == 0):
        soma = j1 + j2
        if soma % 2 != 0:
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")
    elif(r == 1) and (a == 1):
        print("Jogador 2 ganha!")
    elif(r == 1) and (a == 0):
        print("Jogador 1 ganha!")
    elif(r == 0) and (a == 1):
        print("Jogador 1 ganha!")
