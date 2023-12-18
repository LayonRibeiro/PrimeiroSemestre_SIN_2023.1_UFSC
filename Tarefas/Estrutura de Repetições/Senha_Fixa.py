senha = input("Defina sua senha:")

senha1 = input("Digite a senha para acesso:")

if senha != senha1:
    while senha != senha1:
        senha1 = input("Senha Inválida. Digite novamente:")
        
input("Acesso Permitido")