# Crie um dicionário representando um carrinho de compras.
# Adicione produtos (chaves) e quantidades (valores) ao carrinho.
# Calcule o total do carrinho de compra.


lista_compras = {
    'Banana': 7.90, 
    'Suco': 5.49, 
    'Cenoura': 5.00, 
    'Sabonete': 2.59, 
    'Pão': 7.49
}

soma = 0 
for valor in lista_compras.values():
    soma += valor

print(f'Total do carrinho: {soma:.2f}')
