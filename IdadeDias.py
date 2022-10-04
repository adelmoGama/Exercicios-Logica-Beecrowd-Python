# ENTRADA:
idade: int = int(input())
aux: int
# PROCESSAMENTO:
anos: int = int(idade / 365)
aux: int = idade - (anos * 365)
meses: int = int(aux / 30)
aux: int = aux - (meses * 30)
dias: int = aux
# SAÍDA:
print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")
