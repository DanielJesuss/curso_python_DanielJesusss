"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar  Ler  Alterar  apagar = lista[1] - (CRUD)
"""

string = 'ABCDE'

#        0    1      2        3    4
#       -5   -4     -3       -2   -1
lista = [10, 20, 30, 40]
# lista[-3] = 'Daniel Jesus'
# print(lista[2], type(lista[2]))

lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()
print(lista, 'Removido', ultimo_valor)