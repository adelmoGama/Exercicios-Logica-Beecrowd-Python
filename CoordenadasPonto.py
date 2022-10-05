# ENTRADA:
x, y = input().split(" ")
x: float = float(x)
y: float = float(y)
# PROCESSAMENTO:
if(x == 0.0) and (y == 0.0):
    print('Origem')
elif x == 0.0:
    print("Eixo Y")
elif y == 0.0:
    print("Eixo X")
elif x > 0:
    if y > 0:
        print("Q1")
    elif y < 0:
        print("Q4")
elif x < 0:
    if y > 0:
        print("Q2")
    elif y < 0:
        print("Q3")
