idade_usuario = int(input("Digite sua idade: "))

if idade_usuario < 15:
    print("Você é criança")
elif idade_usuario >= 15 and idade_usuario < 20:
    print("Você é adolescente")
elif idade_usuario >=20 and idade_usuario < 60:
    print("Você é adulto")
else:
    print("Você é idoso")