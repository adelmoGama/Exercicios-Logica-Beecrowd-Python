# DADOS:
pi: float = 3.14159
# ENTRADAS:
dados = input().split(" ")
A, B, C = dados
# PROCESSAMENTO:
areaTriangulo: float = (float(A) * float(C)) / 2
areaCirculo: float = pi * (float(C) ** 2)
areaTrapezio: float = ((float(A) + float(B)) * float(C)) / 2
areaQuadrado: float = float(B) ** 2
areaRetangulo: float = float(A) * float(B)
# SAÍDA:
print("TRIANGULO: %.3f" % areaTriangulo)
print("CIRCULO: %.3f" % areaCirculo)
print("TRAPEZIO: %.3f" % areaTrapezio)
print("QUADRADO: %.3f" % areaQuadrado)
print("RETANGULO: %.3f" % areaRetangulo)
