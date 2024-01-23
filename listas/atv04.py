# Crie um dicionário representando contatos (nome, telefone).
# Permita ao usuário procurar por um contato pelo nome.


lista_contatos = {
    'Lais': 80009800,
    'Roger': 89009800,
    'Guilherme': 7890023900,
    'Carla': 789030090
}

#Ternário 

nome_contato = input("Digite o nome do contato: ")
print(f'{nome_contato}: {lista_contatos[nome_contato]}' if nome_contato in lista_contatos else "Nome não encontrado")



# if nome_contato == "Lais":
#     print("Lais:", lista_contatos['Lais'])
# elif nome_contato == "Roger":
#     print("Roger:", lista_contatos['Roger'])
# elif nome_contato == "Guilherme":
#     print("Guilherme:", lista_contatos['Guilherme'])
# elif nome_contato == "Carla":
#     print("Carla:", lista_contatos['Carla'])
# else:
#     print("Nome não encontrado")

