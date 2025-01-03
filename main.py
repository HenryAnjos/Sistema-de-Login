import json

#abrindo o arquivo json dos usuarios no modo leitura "r" e criando a varial "file"
with open ('usuarios.json','r') as file:
    #variavel usuarios e comando pra carregar o arquivo json que esta na variavel file
    usuarios = json.load(file)


#Menu interativo com o user
print('----🔐SISTEMA DE LOGIN----')
print('[1]- Login')
print('[2]- Criação de Usuario')

#Solicita uma opção
opcao = int(input('Escolha uma Opção: '))

#se a opçao do usuario for login:
if opcao ==1:
    user = input('Digite seu nome de usuario: ').strip().lower()
    password = input('Digite sua senha: ').strip()

    if user in usuarios and usuarios[user] == password:
        print(f'Seja bem vindo {user.upper()}!')
    else:
        print('Usuario ou Senha incorreta!')

#se a opcao do usuario for criação de usuario:
elif opcao == 2:
    novo_usuario = input('Digite seu nome de Usuario:').lower().strip()
    
    #verifica se ja existe algum outro usuario com o mesmo nome
    if novo_usuario in usuarios:
        print('Este nome de Usuario ja Existe! Tente outro!')
    
    #criação da senha
    else:
        nova_senha = input('Digite sua Senha: ').strip()
        
        #adiciona o novo usuario e senha ao arquivo .json
        usuarios[novo_usuario] = nova_senha
        
    #salva no arquivo .json o novo usuario e senha  
    with open('usuarios.json','w') as file:
            json.dump(usuarios,file)
    print(f'Novo Usuario Registrado com Sucesso, Seja Bem Vindo {novo_usuario}')
else: 
    print('Digite 1 ou 2')