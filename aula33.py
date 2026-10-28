"""Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. 
Caso o usuário não digite um número inteiro, informe que não é um número inteiro."""

'''
numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('O número é par')
    else:
        print('O número é impar')
else:
    print('Você não digitou um número inteiro')
'''

"""Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. 
Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23."""

'''
hora = input('Digite a hora: ')

try:
    hora = int(hora)

    if hora >= 0 and hora <= 5:
        print('Está de madrugada')
    elif hora >= 6 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 18:
        print('Boa tarde')
    elif hora >= 19 and hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas numeros inteiros')
'''

"""Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva 
'Seu nome é curto'; se tiver entre 5 e 6 letras, escreva 'Seu nome é normal'; maior que 6 escreva 
'Seu nome é muito grande"""

'''
nome = input('Digite o seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) == 5 or len(nome) == 6:
    print('Seu nome é normal')
elif len(nome) > 7:
    print('Seu nome é muito grande') 
'''