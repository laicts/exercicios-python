turno = input("Qual turno você estuda? Digite M para matutino, V para vespertino ou N para noturno: ")

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa Tarde")
elif turno == "N":
    print("Boa Noite")
else:
    print("Valor inválido!")