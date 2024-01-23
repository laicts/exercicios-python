pares = 0
impares = 0

while True:
    try:
        numero = int(input("Digite um número: "))

        if numero == 0:
            break
        if numero < 0:
            print("Insira um número positivo")
            numero = int(input("Digite um número: "))
        
        if numero % 2 == 0:
            pares += 1 
        else:
            impares += 1
    except ValueError:
        print("Insira um número válido")


print(f'Quantidade de números pares: {pares}')
print(f'Quantidade de números impares: {impares}')

      

    

