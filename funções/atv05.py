# Crie uma função chamada contar_vogais que recebe uma string
# como parâmetro. Implemente a lógica para contar o número de vogais
# na string e retorne o total de vogais. Solicite ao usuário para inserir uma
# frase e utilize a função para contar as vogais.



def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    total_vogais = sum(1 for char in frase if char in vogais) 
    # o sum é uma função que percorre e acrescenta um na contagem, o for char in frase percorre cada char na string frase, se o caractere conter na string vogal, ele acrescenta um na contagem
    return total_vogais

frase = input("Digite uma frase: ")

resultado = contar_vogais(frase)
print(f'Total de vogais na frase: {resultado}')





