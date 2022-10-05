pa: int = 0
im: int = 0
po: int = 0
ne: int = 0
for i in range(5):
    numero: int = int(input())
    if numero > 0:
        po += 1
    elif numero < 0:
        ne += 1
    if numero % 2 == 0:
        pa += 1
    elif numero % 2 != 0:
        im += 1
print(pa, "valor(es) par(es)")
print(im, "valor(es) impar(es)")
print(po, "valor(es) positivo(s)")
print(ne, "valor(es) negativo(s)")
