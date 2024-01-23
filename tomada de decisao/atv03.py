numero_pedido = int(input("Digite um número entre 0 e 10: "))

while numero_pedido > 10 or numero_pedido < 0:
    print("Número inválido!")
    numero_pedido = int(input("Digite um número entre 0 e 10: "))
    
