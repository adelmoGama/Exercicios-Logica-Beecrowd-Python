C: int = int(input())
for i in range(C):
    nome, forca = input().split(" ")
    nome: str = str(nome).upper()
    forca: int = int(forca)
    if nome == "THOR":
        print("Y")
    else:
        print("N")
