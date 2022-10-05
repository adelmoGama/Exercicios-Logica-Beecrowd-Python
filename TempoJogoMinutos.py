horaInicial, minutoInicial, horaFinal, minutoFinal = input().split()
horaInicial, minutoInicial = int(horaInicial), int(minutoInicial)
horaFinal, minutoFinal = int(horaFinal), int(minutoFinal)
hora: int = 0
minuto: int = 0
if horaInicial < horaFinal:
    hora = horaFinal - horaInicial
    if minutoInicial < minutoFinal:
        minuto = minutoFinal - minutoInicial
    if minutoInicial > minutoFinal:
        hora = hora - 1
        minuto = (60 - minutoInicial) + minutoFinal
    if minutoInicial == minutoFinal:
        minuto = 0
if horaInicial > horaFinal:
    hora = (24 - horaInicial) + horaFinal
    if minutoInicial < minutoFinal:
        minuto = minutoFinal - minutoInicial
    if minutoInicial > minutoFinal:
        hora = hora - 1
        minuto = (60 - minutoInicial) + minutoFinal
    if minutoInicial == minutoFinal:
        minuto = 0
if horaInicial == horaFinal:
    if minutoInicial < minutoFinal:
        minuto = minutoFinal - minutoInicial
        hora = 0
    if minutoInicial > minutoFinal:
        minuto = (60 - minutoInicial) + minutoFinal
        hora = 23
    if minutoInicial == minutoFinal:
        hora = 24
        minuto = 0
print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")

# # ENTRADA:
# horaInicial, minutoInicial, horaFinal, minutoFinal = input().split(" ")
# horaInicial: int = int(horaInicial)
# minutoInicial: int = int(minutoInicial)
# horaFinal: int = int(horaFinal)
# minutoFinal: int = int(minutoFinal)
# # PROCESSAMENTO:
# if horaFinal > horaInicial:
#     hora: int = horaFinal - horaInicial
#     if minutoFinal > minutoInicial:
#         minuto = minutoFinal - minutoInicial
#     elif minutoFinal == minutoInicial:
#         minuto = 0
#     else:
#         minuto: int = 60 + (minutoFinal - minutoInicial)
#         hora -= 1
#     print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")
# elif horaFinal == horaInicial:
#     hora = 24
#     if minutoFinal > minutoInicial:
#         minuto: int = minutoFinal - minutoInicial
#     elif minutoFinal == minutoInicial:
#         minuto = 0
#     else:
#         minuto: int = 60 + (minutoFinal - minutoInicial)
#         hora -= 1
#     print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")
# elif horaInicial > horaFinal:
#     hora: int = 24 + (horaFinal - horaInicial)
#     if minutoFinal > minutoInicial:
#         minuto: int = minutoFinal - minutoInicial
#     elif minutoFinal == minutoInicial:
#         minuto = 0
#     else:
#         minuto: int = 60 + (minutoFinal - minutoInicial)
#         hora -= 1
#     print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")
