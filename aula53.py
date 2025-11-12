"""
enumerate - enumera iteráveis (indices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


for item in list(enumerate(lista)):
    indice, nome = item
    print(indice, nome)