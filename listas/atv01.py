perguntas = [
    input(("Telefonou para a vítima?")),
    input(("Esteve no local do crime?")),
    input(("Mora perto da vítima?")),
    input(("Devia para a vítima?")),
    input(("Já trabalhou com a vítima?"))
]

resposta = 0

for pergunta in perguntas:
    if pergunta.lower() == "sim":
        resposta += 1

if resposta == 2:
    print("Você é suspeito")
elif resposta >= 3 and resposta <=4:
    print("Você é cúmplice")
elif resposta == 5:
    print("Você é o assassino")
else:
    print("Você é inocente")
    