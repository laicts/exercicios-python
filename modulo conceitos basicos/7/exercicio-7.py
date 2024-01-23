peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura *altura)

print(f'Seu índice de massa corporal é {imc:.2f}')