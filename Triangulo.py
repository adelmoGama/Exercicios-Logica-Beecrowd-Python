A, B, C, D = input().split(" ")
A, B, C, D = int(A), int(B), int(C), int(D)
if(A > abs(B - C)) and (A < (B + C)) or (A > abs(B - D)) and (A < (B + D)) or (A > abs(C - D)) and (A < (C + D)):
    print("S")
elif(B > abs(A - C)) and (B < (A + C)) or (B > abs(A - D)) and (B < (A + D)) or (B > abs(C - D)) and (B < (C + D)):
    print("S")
elif(C > abs(A - B)) and (C < (A + B)) or (C > abs(B - D)) and (C < (B + D)) or (C > abs(A - D)) and (C < (A + D)):
    print("S")
elif(D > abs(A - B)) and (D < (A + B)) or (D > abs(A - C)) and (D < (A + C)) or (D > abs(B - C)) and (D < (B + C)):
    print("S")
else:
    print("N")
