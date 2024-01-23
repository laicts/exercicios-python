salarioBruto = float(input('Digite o valor do salário bruto: '))

if salarioBruto <= 1903.98:
    print('Isento de imposto')
elif salarioBruto <= 2826.65:
    desconto = (salarioBruto * 7.5) / 100
    liquido = salarioBruto - desconto
    print(f'O salário liquido é: {liquido}')
elif salarioBruto <= 3751.05:
    desconto = (salarioBruto * 15) / 100
    liquido = salarioBruto - desconto
    print(f'O salário liquido é: {liquido}')
elif salarioBruto <= 4664.68:
    desconto = (salarioBruto * 22.5) / 100
    liquido = salarioBruto - desconto

    print(f'O salário liquido é: {liquido}')
else:
    desconto = (salarioBruto * 27.5) / 100
    liquido = salarioBruto - desconto
    print(f'O salário liquido é: {liquido}')
