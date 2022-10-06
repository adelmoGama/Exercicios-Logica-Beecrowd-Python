I = 0
J = 0
while I < 2:
    for i in range(3):
        J += 1
        if I > 1.8:
            I = 2
        if I == 0 or I == 1 or I == 2:
            print("I=%d J=%d" % (I, J+I))
        else:
            print("I=%.1f J=%.1f" % (I, J+I))
    I += 0.2
    J = 0
