# Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira, e calcule quanto poderia comprar de cada moeda estrangeira.

conversoes = {
        'Dólar Americano': 4.91,
        'Peso Argentino': 0.02,
        'Dólar Australiano': 3.18,
        'Dólar Canadense': 3.64,
        'Franco Suiço': 0.42,
        'Euro': 5.36,
        'Libra esterlina': 6.21
    }

def calcular_conversao (valor_carteira, taxa_conversao):
    return valor_carteira / taxa_conversao

carteira = float(input("Digite o valor disponível na carteira: "))

for moeda, taxa in conversoes.items():
    quantidade = calcular_conversao(carteira, taxa)
    print(f'{carteira} pode comprar: {moeda} {quantidade:.2f}')



