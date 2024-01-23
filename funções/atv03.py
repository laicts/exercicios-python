# Escreva um script que pergunta ao usuário se ele deseja converter
# uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
# cada opção, crie uma função.


def convertFunction (temperatura):
    if temperatura.lower() == "celsius":
        return celsius_converter()
    elif temperatura.lower() == "fahrenheit":
        return Fahrenheit_converter()
    else:
        print("Unidade de temperatura inválida. Escolha entre Celsius e Fahrenheit.")


def Fahrenheit_converter():
    try:
        graus = float(input("Digite uma temperatura em graus Celsius: "))
        convert_to_fahrenheit = (graus * 1.8) + 32
        print(f'A temperatura em Graus Fahrenheit é: {convert_to_fahrenheit:.2f}°')
    except ValueError:
        print("Por favor, insira um número válido.")

def celsius_converter():
    try:
        graus = float(input("Digite a temperatura em Fahrenheit: "))
        convert_to_celsius = (graus - 32) / 1.8 
        print(f'A temperatura em Graus Celsius é: {convert_to_celsius:.2f}°')
    except ValueError:
        print("Por favor, insira um número válido.")

convertFunction(temperatura = input("Qual unidade de temperatura deseja converter?:  "))