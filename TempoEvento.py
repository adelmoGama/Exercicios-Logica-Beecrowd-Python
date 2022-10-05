texto1, diaInicio = input().split(" ")
diaInicio = int(diaInicio)
horaInicial, minutoInicial, segundoInicial = input().split(":")
horaInicial, minutoInicial, segundoInicial = int(horaInicial), int(minutoInicial), int(segundoInicial)
texto2, diaFinal = input().split(" ")
diaFinal = int(diaFinal)
horaFinal, minutoFinal, segundoFinal = input().split(":")
horaFinal, minutoFinal, segundoFinal = int(horaFinal), int(minutoFinal), int(segundoFinal)
# VARIAVEIS:
dia = 0
hora = 0
minuto = 0
segundo = 0
# CASO 1: DIA FINAL MAIOR QUE O DIA INICIAL:
if diaFinal > diaInicio:
    dia = diaFinal - diaInicio
    if horaFinal > horaInicial:
        hora = horaFinal - horaInicial
        if minutoFinal > minutoInicial:
            minuto = minutoFinal - minutoInicial
            if segundoFinal > segundoInicial:
                segundo = segundoFinal - segundoInicial
            elif segundoFinal == segundoInicial:
                segundo = segundoFinal - segundoInicial
            elif segundoFinal < segundoInicial:
                segundo = 60 + (segundoFinal - segundoInicial)
                minuto -= 1
        elif minutoFinal == minutoInicial:
            minuto = minutoFinal - minutoInicial
            if segundoFinal > segundoInicial:
                segundo = segundoFinal - segundoInicial
            elif segundoFinal == segundoInicial:
                segundo = segundoFinal - segundoInicial
            elif segundoFinal < segundoInicial:
                segundo = 60 + (segundoFinal - segundoInicial)
                minuto += 59
                hora -= 1
        elif minutoFinal < minutoInicial:
            if segundoFinal > segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = 60 + (minutoFinal - minutoInicial)
                hora = (horaFinal - 1) - horaInicial
            elif segundoFinal == segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = 60 + (minutoFinal - minutoInicial)
                hora = (horaFinal - 1) - horaInicial
            elif segundoFinal < segundoInicial:
                segundo = 60 + (segundoFinal - segundoInicial)
                minuto = 60 + ((minutoFinal - 1) - minutoInicial)
                hora -= 1
    elif horaFinal == horaInicial:
        hora = horaFinal - horaInicial
        if minutoFinal > minutoInicial:
            minuto = minutoFinal - minutoInicial
            if segundoFinal > segundoInicial:
                segundo = segundoFinal - segundoInicial
            elif segundoFinal == segundoInicial:
                segundo = segundoFinal - segundoInicial
            elif segundoFinal < segundoInicial:
                segundo = 60 + (segundoFinal - segundoInicial)
                minuto -= 1
        elif minutoFinal == minutoInicial:
            minuto = minutoFinal - minutoInicial
            if segundoFinal > segundoInicial:
                segundo = segundoFinal - segundoInicial
            elif segundoFinal == segundoInicial:
                segundo = segundoFinal - segundoInicial
            elif segundoFinal < segundoInicial:
                segundo = 60 + (segundoFinal - segundoInicial)
                minuto = 60 + ((minutoFinal - 1) - minutoInicial)
                hora = 24 + ((horaFinal - 1) - horaInicial)
                dia -= 1
        elif minutoFinal < minutoInicial:
            if segundoFinal > segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = 60 + (minutoFinal - minutoInicial)
                hora = 24 + ((horaFinal - 1) - horaInicial)
                dia -= 1
            elif segundoFinal == segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = 60 + (minutoFinal - minutoInicial)
                hora = 24 + ((horaFinal - 1) - horaInicial)
                dia -= 1
            elif segundoFinal < segundoInicial:
                segundo = 60 + (segundoFinal - segundoInicial)
                minuto = 60 + ((minutoFinal - 1) - minutoInicial)
                hora = 24 + ((horaFinal - 1) - horaInicial)
                dia -= 1
    elif horaFinal < horaInicial:
        if minutoFinal > minutoInicial:
            if segundoFinal > segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = minutoFinal - minutoInicial
                hora = 24 + (horaFinal - horaInicial)
                dia -= 1
            elif segundoFinal == segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = minutoFinal - minutoInicial
                hora = 24 + (horaFinal - horaInicial)
                dia -= 1
            elif segundoFinal < segundoInicial:
                segundo = 60 + (segundoFinal - segundoInicial)
                minuto = ((minutoFinal - 1) - minutoInicial)
                hora = 24 + (horaFinal - horaInicial)
                dia -= 1
        elif minutoFinal == minutoInicial:
            if segundoFinal > segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = minutoFinal - minutoInicial
                hora = 24 + (horaFinal - horaInicial)
                dia -= 1
            elif segundoFinal == segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = minutoFinal - minutoInicial
                hora = 24 + (horaFinal - horaInicial)
                dia -= 1
            elif segundoFinal < segundoInicial:
                segundo = 60 + (segundoFinal - segundoInicial)
                minuto = (60 + (minutoFinal - 1) - minutoInicial)
                hora = 24 + ((horaFinal - 1) - horaInicial)
                dia -= 1
        elif minutoFinal < minutoInicial:
            if segundoFinal > segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = 60 + (minutoFinal - minutoInicial)
                hora = 24 + ((horaFinal - 1) - horaInicial)
                dia -= 1
            elif segundoFinal == segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = 60 + (minutoFinal - minutoInicial)
                hora = 24 + ((horaFinal - 1) - horaInicial)
                dia -= 1
            elif segundoFinal < segundoInicial:
                segundo = 60 + (segundoFinal - segundoInicial)
                minuto = 60 + ((minutoFinal - 1) - minutoInicial)
                hora = 24 + ((horaFinal - 1) - horaInicial)
                dia -= 1
elif diaFinal == diaInicio:
    if horaFinal > horaInicial:
        if minutoFinal > minutoInicial:
            if segundoFinal > segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = minutoFinal - minutoInicial
                hora = horaFinal - horaInicial
                dia = diaFinal - diaInicio
            elif segundoFinal == segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = minutoFinal - minutoInicial
                hora = horaFinal - horaInicial
                dia = diaFinal - diaInicio
            elif segundoFinal < segundoInicial:
                segundo = 60 + (segundoFinal - segundoInicial)
                minuto = (minutoFinal - 1) - minutoInicial
                hora = horaFinal - horaInicial
                dia = diaFinal - diaInicio
        elif minutoFinal == minutoInicial:
            if segundoFinal > segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = minutoFinal - minutoInicial
                hora = horaFinal - horaInicial
                dia = diaFinal - diaInicio
            elif segundoFinal == segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = minutoFinal - minutoInicial
                hora = horaFinal - horaInicial
                dia = diaFinal - diaInicio
        elif minutoFinal < minutoInicial:
            if segundoFinal > segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = 60 + (minutoFinal - minutoInicial)
                hora = (horaFinal - 1) - horaInicial
                dia = diaFinal - diaInicio
            elif segundoFinal == segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = 60 + (minutoFinal - minutoInicial)
                hora = (horaFinal - 1) - horaInicial
                dia = diaFinal - diaInicio
            elif segundoFinal < segundoInicial:
                segundo = 60 + (segundoFinal - segundoInicial)
                minuto = 60 + ((minutoFinal - 1) - minutoInicial)
                hora = (horaFinal - 1) - horaInicial
                dia = diaFinal - diaInicio
    elif horaFinal == horaInicial:
        if minutoFinal > minutoInicial:
            if segundoFinal > segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = minutoFinal - minutoInicial
                hora = horaFinal - horaInicial
                dia = diaFinal - diaInicio
            elif segundoFinal == segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = minutoFinal - minutoInicial
                hora = horaFinal - horaInicial
                dia = diaFinal - diaInicio
            elif segundoFinal < segundoInicial:
                segundo = 60 + (segundoFinal - segundoInicial)
                minuto = (minutoFinal - 1) - minutoInicial
                hora = horaFinal - horaInicial
                dia = diaFinal - diaInicio
        elif minutoFinal == minutoInicial:
            if segundoFinal > segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = minutoFinal - minutoInicial
                hora = horaFinal - horaInicial
                dia = diaFinal - diaInicio
            elif segundoFinal == segundoInicial:
                segundo = segundoFinal - segundoInicial
                minuto = minutoFinal - minutoInicial
                hora = horaFinal - horaInicial
                dia = diaFinal - diaInicio
print(f"{dia} dia(s)\n{hora} hora(s)\n{minuto} minuto(s)\n{segundo} segundo(s)")
