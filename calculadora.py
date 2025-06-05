# Calculadora EX.1
#Copiar e colar arquivo google colab.

# 1. Vamos realizar um cadastro simples, com o nome e ano de nascimento do novo usuário.
# informações inportantes: ano atual é 2025
ano = 2025
nome_usuario = input("Digite seu nome: ") # o novo usuário insere seu nome
while True: #Loop até o usuário inserir uma ano de nascimento válido
  ano_usuario = int(input("Digite seu ano de nascimento: ")) # o novo usuário insere o ano de nascimento
  idade = ano - (ano_usuario) # calcula a idade do novo usuário
  if idade < 18: #condição que faz refazer a pergunta até ter uma resposta válida
    print('Informação inválida, é necessário ter mais de 18 anos para acessar a plataforma')
  else: #Quando for inserida a resposta válida para de perguntar a idade
    break
if idade >= 18: # se a idade for maior ou igual a 18 isso garante o cadastro
  print(f"Cadastro realizado com sucesso, {nome_usuario}!")
mae_usuario = input("Digite o nome da sua mãe: ") # o novo usuário insere o nome da mãe
# Para cadastrar a mãe, a diferença de idade entre a mãe e filho(a) tem que ser pelo menos 14 anos, por isso vou criar uma condição que garanta essa diferença de idade
while True: #loop para conseguir garantir uma diferença de idade de pelo menos 14 anos entre a mãe e a filha
  ano_mae = int(input("Digite o ano de nascimento da sua mãe: ")) # o novo usuário insere o ano de nascimento da mãe
  idade_mae = ano - (ano_mae) #para saber quantos anos a mãe tem
  if idade_mae - idade < 14: #Se a idade da mãe for menos que 14 a operação vai ser inválida
    print('Informação inválida. A diferença de idade entre a mãe e filho(a) tem que ser pelo menos 14 anos.')
  else: #Quando for inserida a resposta válida para de perguntar a idade da mãe
    break
print(f"{nome_usuario}, você e sua mãe {mae_usuario}, possuem {idade_mae - idade} anos de diferença de idade.")
pai_usuario = input("Digite o nome do seu pai: ") # o novo usuário insere o nome do pai
# Para cadastrar o pai a diferença de idade entre o pai e a filha tem que ser pelo menos 14 anos, por isso vou criar uma condição que garanta essa diferença de idade
while True: #loop para conseguir garantir uma diferença de idade de pelo menos 14 anos entre o pai e a filha
  ano_pai = int(input("Digite o ano de nascimento de seu pai: ")) # o novo usuário insere o ano de nascimento do pai
  idade_pai = ano - (ano_pai) #para saber quantos anos o pai tem
  if idade_pai - idade < 14: #Se a idade do pai for menos que 14 a operação vai ser inválida
    print('Informação inválida. A diferença de idade entre o pai e filho(a) tem que ser pelo menos 14 anos.')
  else: #Quando for inserida a resposta válida para de perguntar a idade do pai
    break
print(f"{nome_usuario}, você e seu pai {pai_usuario}, possuem {idade_pai - idade} anos de diferença de idade, sabia dessa informação?")
diferenca = abs(idade_pai - idade_mae) #Código para ter sempre um número positivo, vamos usar essa informação para falar a diferença de idade.
if idade_pai == idade_mae:#condição para saber se o pai e a mãe tem a mesma idade
  print(f"{nome_usuario}, você sabia que {pai_usuario} e {mae_usuario} possuem a mesma idade")
else: #se a idade for diferente
  print(f"{nome_usuario}, você sabia que {pai_usuario} e {mae_usuario} possuem {diferenca} ano{'s' if diferenca != 1 else ''} de diferença de idade?")
print(f"{nome_usuario}, a idade média de vocês três é {(idade + idade_mae + idade_pai)/3:.2f} anos.") # Aqui usei suma e divisão par descobria a idade média deles.

# Para usar a operação de divisão, vamos verificar se os anos de nascimento são bissextos
# Um ano é bissexto se for divisível por 4 e não for divisível por 100, exceto se for divisível por 400.

verificar_bissextos = input(f"{nome_usuario}, você gostaria de saber se os anos são bissextos?:(sim/não)").lower()# Pergunta para o usuário responder se quer continuar ou não
if verificar_bissextos == "sim":
  if (ano_usuario % 4 == 0 and ano_usuario % 100 != 0) or ano_usuario % 400 == 0: #calculo de verificação de ano bissexto e condição
    print(f"{ano_usuario} é um ano bissexto")
  else:
    print(f"{ano_usuario} não é um ano bissexto")
    #verificação da mãe
  if (ano_mae % 4 == 0 and ano_mae % 100 != 0) or ano_mae % 400 == 0: #calculo de verificação de ano bissexto e condição
    print(f"{ano_mae} é um ano bissexto")
  else:
    print(f"{ano_mae} não é um ano bissexto")
    #verificação pai
  if (ano_pai % 4 == 0 and ano_pai % 100 != 0) or ano_pai % 400 == 0:#calculo de verificação de ano bissexto e condição
    print(f"{ano_pai} é um ano bissexto")
  else:
    print(f"{ano_pai} não é um ano bissexto")
else: #Condição caso a resposta seja não
    print("Ok, até a próxima!")

# Para usar a operação de multiplicação (*), vamos calcular quantos meses de vida cada pessoa possui.
#Para verificar quantos meses de vida a pessoa possui basta multiplicar o quantos anos eles tem pelo numero 12 (que representa quantos meses tem em uma ano).

verificar_meses = input(f"{nome_usuario}, você gostaria de saber quantos meses de vida você possui?:(sim/não)").lower() # Pergunta para o usuário responder se quer continuar ou não
if verificar_meses == "sim": #condição para realização da somatória
  meses_usuario = idade * 12 #calculo
  meses_mae = idade_mae * 12 #calculo
  meses_pai = idade_pai * 12 #calculo
  print(f"{nome_usuario}, você possui {meses_usuario} meses de vida, já {mae_usuario}, possui {meses_mae} meses de vida e seu pai {pai_usuario}, possui {meses_pai} meses de vida")
  print(f"Vocês três juntos possuem {meses_usuario + meses_mae + meses_pai} meses de vida") #frase com a função matemática de soma
else:
  print("Ok, até a próxima!")

