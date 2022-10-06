opcao: int = 1
while opcao == 1:
    while True:
        nota1: float = float(input())
        while(nota1 > 10) or (nota1 < 0):
            print("nota invalida")
            nota1 = float(input())
        nota2: float = float(input())
        while(nota2 > 10) or (nota2 < 0):
            print("nota invalida")
            nota2 = float(input())
        media: float = float((nota1 + nota2) / 2)
        print("media = %.2f" % media)
        print("novo calculo (1-sim 2-nao)")
        opcao = int(input())
        while(opcao != 1) and (opcao != 2):
            print("novo calculo (1-sim 2-nao)")
            opcao = int(input())
        if opcao == 2:
            break
