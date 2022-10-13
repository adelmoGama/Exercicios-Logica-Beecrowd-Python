a, b = input().split(" ")
a, b = int(a), int(b)
if b < 0:
    b *= -1
    q = (a // b) * (-1)
    r = a % b
else:
    q = (a // b)
    r = a % b
print(q, r)
