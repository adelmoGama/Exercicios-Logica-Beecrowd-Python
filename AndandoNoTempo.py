A, B, C = input().split()
A, B, C = int(A), int(B), int(C)
if(A == B == C) or (A == B) or (A == C) or (B == C):
    print("S")
elif((A+B) == C) or ((A+C) == B) or ((B+C) == A):
    print("S")
else:
    print("N")
