I = int(input())
frase = "Feliz natal!"
frase = list(frase)
for k in range(I-1):
    frase.insert(9, "a")
for i in frase:
    print(i, end="")
print("")
