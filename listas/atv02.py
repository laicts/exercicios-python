# Faça um Programa que peça as quatro notas de 5 alunos, calcule
# e armazene numa lista a média de cada aluno, imprima o número
# de alunos com média maior ou igual a 7.0.

media_alunos = []

def notas_cada_aluno():
    print("Informe as notas do aluno ")
    notas_aluno = [
    float(input("Nota 1: ")),
    float(input("Nota 2: ")),
    float(input("Nota 3: ")),
    float(input("Nota 4: ")),
]
    soma = 0
    for nota in notas_aluno:
        soma += nota

    media = soma / 4
    if media >= 7.0:
        media_alunos.append(media)


for i in range(5):
    notas_cada_aluno()


print(media_alunos)