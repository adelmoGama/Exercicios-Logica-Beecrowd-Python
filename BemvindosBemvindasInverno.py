A, B, C = input().split(" ")
A, B, C = int(A), int(B), int(C)
if A > B:
    if B <= C:
        print(":)")
    elif B > C:
        if(B - C) < (A - B):
            print(":)")
        elif(B - C) >= (A - B):
            print(":(")
elif A < B:
    if B >= C:
        print(":(")

    elif(C - B) < (B - A):
        print(":(")
    elif(C - B) >= (B - A):
        print(":)")
elif A == B:
    if C > B:
        print(":)")
    else:
        print(":(")
