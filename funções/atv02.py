# Reverso do número. Faça uma função que retorne o reverso de um
# número inteiro informado. Por exemplo: 127 -> 721.


def inverteNum (numero):
    numero = str(numero) #converte o numero em string
    numero_invertido = numero[::-1] #inverte a string
    numero_inteiro = int(numero_invertido) #converte a string em número novamente
    print(f"Numero invertido: {numero_inteiro}")
    return numero_inteiro
    


inverteNum(numero = int(input("Digite um número: ")))