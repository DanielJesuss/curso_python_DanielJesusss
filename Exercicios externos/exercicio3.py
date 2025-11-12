"""
Crie um programa que peça uma senha ao usuário. 
Enquanto ele não digitar "python123", o programa
 deve continuar pedindo. Quando acertar, 
 exiba "Acesso permitido
"""

senha_correta = 'python123'
senha_digitada = 0

while senha_digitada != senha_correta:
    senha_digitada = input('Digite a senha: ')
    print('Acesso negado')


print('Acesso permitido')
