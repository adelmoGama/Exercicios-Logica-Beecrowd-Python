opcao: int = 0
alcool: int = 0
gasolina: int = 0
diesel: int = 0
while True:
    if opcao == 4:
        break
    if opcao == 1:
        alcool += 1
        print("a")
    elif opcao == 2:
        gasolina += 1
        print("g")
    elif opcao == 3:
        diesel += 1
        print("d")
    opcao = int(input())
print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
