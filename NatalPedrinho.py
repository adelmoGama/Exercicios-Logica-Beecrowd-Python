while True:
    try:
        mes, dia = input().split()
        mes, dia = int(mes), int(dia)
        passou: int = 0
        if mes == 1:
            passou += dia
            print(f"Faltam {360 - passou} dias para o natal!")
        elif mes == 2:
            passou += 31 + dia
            print(f"Faltam {360 - passou} dias para o natal!")
        elif mes == 3:
            passou += 60 + dia
            print(f"Faltam {360 - passou} dias para o natal!")
        elif mes == 4:
            passou += 91 + dia
            print(f"Faltam {360 - passou} dias para o natal!")
        elif mes == 5:
            passou += 121 + dia
            print(f"Faltam {360 - passou} dias para o natal!")
        elif mes == 6:
            passou += 152 + dia
            print(f"Faltam {360 - passou} dias para o natal!")
        elif mes == 7:
            passou += 182 + dia
            print(f"Faltam {360 - passou} dias para o natal!")
        elif mes == 8:
            passou += 213 + dia
            print(f"Faltam {360 - passou} dias para o natal!")
        elif mes == 9:
            passou += 244 + dia
            print(f"Faltam {360 - passou} dias para o natal!")
        elif mes == 10:
            passou += 274 + dia
            print(f"Faltam {360 - passou} dias para o natal!")
        elif mes == 11:
            passou += 305 + dia
            print(f"Faltam {360 - passou} dias para o natal!")
        elif mes == 12:
            passou += 335 + dia + 1
            if passou == 360:
                print("E vespera de natal!")
            elif passou == 361:
                print("E natal!")
            elif passou > 361:
                print("Ja passou!")
            else:
                print(f"Faltam {360 - passou} dias para o natal!")
    except EOFError:
        break
