"""
Desempacotamento em chamadas de metódos e funções
"""

string ='ABC'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Pyton', 'é', 'legal'

salas = [
    # 0        1
    ['Maria', 'Helena',],  # 0
   #  0        
    ['Elaine',],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda',],  # 2
]

# a, b, *_, u= lista
# print(a, u)

# for nome in lista:
#     print(nome, end=' ',)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')