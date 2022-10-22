S = input()
S = list(S)
qtd = S.count("1")
if qtd % 2 == 0:
    S.append("0")
else:
    S.append("1")
for i in range(int(len(S))):
    print(S[i], end="")
print('')
