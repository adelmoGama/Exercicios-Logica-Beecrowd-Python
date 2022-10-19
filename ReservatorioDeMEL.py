while True:
    try:
        V: float = float(input())
        D: float = float(input())
        area: float = 3.14 * ((D/2)**2)
        altura: float = V / area
        print("ALTURA = %.2f" % altura)
        print("AREA = %.2f" % area)
    except EOFError:
        break
