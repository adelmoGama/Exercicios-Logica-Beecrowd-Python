T = int(input())
cont = 0
for i in range(T):
    s, r = input().lower().split(" ")
    cont += 1
    if s == 'pedra':
        if r == 'pedra':
            print(f"Caso #{cont}: De novo!")
        elif(r == 'spock') or (r == 'papel'):
            print(f"Caso #{cont}: Raj trapaceou!")
        else:
            print(f"Caso #{cont}: Bazinga!")
    elif s == 'papel':
        if(r == 'pedra') or (r == 'spock'):
            print(f"Caso #{cont}: Bazinga!")
        elif r == 'papel':
            print(f"Caso #{cont}: De novo!")
        else:
            print(f"Caso #{cont}: Raj trapaceou!")
    elif s == 'tesoura':
        if(r == 'papel') or (r == 'lagarto'):
            print(f"Caso #{cont}: Bazinga!")
        elif r == 'tesoura':
            print(f"Caso #{cont}: De novo!")
        else:
            print(f"Caso #{cont}: Raj trapaceou!")
    elif s == 'lagarto':
        if(r == 'spock') or (r == 'papel'):
            print(f"Caso #{cont}: Bazinga!")
        elif r == 'lagarto':
            print(f"Caso #{cont}: De novo!")
        else:
            print(f"Caso #{cont}: Raj trapaceou!")
    elif s == 'spock':
        if(r == 'tesoura') or (r == 'pedra'):
            print(f"Caso #{cont}: Bazinga!")
        elif r == 'spock':
            print(f"Caso #{cont}: De novo!")
        else:
            print(f"Caso #{cont}: Raj trapaceou!")
