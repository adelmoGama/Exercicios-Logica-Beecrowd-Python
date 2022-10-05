# ENTRADA:
p1 = input().lower()
p2 = input().lower()
p3 = input().lower()
# PROCESSAMENTO:
if p1 == 'vertebrado':
    if p2 == 'ave':
        if p3 == 'carnivoro':
            print("aguia")
        else:
            print("pomba")
    else:
        if p3 == 'onivoro':
            print("homem")
        else:
            print("vaca")
else:
    if p2 == 'inseto':
        if p3 == 'hematofago':
            print("pulga")
        else:
            print("lagarta")
    else:
        if p3 == 'hematofago':
            print("sanguessuga")
        else:
            print("minhoca")
