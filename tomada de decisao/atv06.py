usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if usuario != "admin" and senha != "admin123":
    print("Usuário e senha incorretos")
else: 
    print("Usuário e senha correta!")