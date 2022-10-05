# ENTRADA:
valor1, valor2, valor3 = input().split(" ")
valor1: int = int(valor1)
valor2: int = int(valor2)
valor3: int = int(valor3)
maior: int
# PROCESSAMENTO:
if valor1 > valor2:
    if valor1 > valor3:
        if valor3 > valor2:
            print(f"{valor2}\n{valor3}\n{valor1}")
        else:
            print(f"{valor3}\n{valor2}\n{valor1}")
    else:
        print(f"{valor2}\n{valor1}\n{valor3}")
else:
    # V2 > V1:
    if valor2 > valor3:
        if valor3 > valor1:
            print(f"{valor1}\n{valor3}\n{valor2}")
        else:
            print(f"{valor3}\n{valor1}\n{valor2}")
    else:
        print(f"{valor1}\n{valor2}\n{valor3}")
print(f"\n{valor1}\n{valor2}\n{valor3}")
