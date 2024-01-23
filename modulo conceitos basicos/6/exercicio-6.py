viagem_distancia = float(input('Qual a distância da viagem: '))

tempo_aviao = viagem_distancia / 600
tempo_carro = viagem_distancia / 100
tempo_onibus = viagem_distancia / 80

print(f'O tempo da viagem de avião é: {tempo_aviao:.2f} horas')
print(f'O tempo da viagem de carro é: {tempo_carro:.2f} horas')
print(f'O tempo da viagem de ônibus é: {tempo_onibus:.2f} horas')