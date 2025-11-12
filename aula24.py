# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 
#  D A N I E L
# -6-5-4-3-2-1

#nome = 'Daniel'
#print(nome[2])
#print(nome[-4])
#print('a' in nome)
#print('b' in nome)
#print('t' not in nome)
#print('a' not in nome)

nome = input('Digite seu nom: ')
encontrar = input('O que quer encontrar? ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')