while True:
    T = int(input())
    if T == 0:
        break
    total = 0
    for i in range(T):
        dados = input().split()
        N = int(dados[0])
        alimento = ''
        for k in range(int(len(dados))):
            if(k > 0) and (k < int(len(dados)) - 1):
                alimento += dados[k]
                alimento += " "
            elif k == (int(len(dados)) - 1):
                alimento += dados[k]
        if alimento == 'suco de laranja':
            total += N * 120
        elif alimento == 'morango fresco':
            total += N * 85
        elif alimento == 'mamao':
            total += N * 85
        elif alimento == 'goiaba vermelha':
            total += N * 70
        elif alimento == 'manga':
            total += N * 56
        elif alimento == 'laranja':
            total += N * 50
        elif alimento == 'brocolis':
            total += N * 34
    if total > 130:
        X = total - 130
        print(f"Menos {X} mg")
    elif total < 110:
        X = 110 - total
        print(f"Mais {X} mg")
    elif(total >= 110) and (total <= 130):
        print(f"{total} mg")
