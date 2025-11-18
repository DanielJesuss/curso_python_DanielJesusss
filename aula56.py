"""
split e join com list e str
split - divide uma string
join = une uma string
"""
frase = 'Olha só que, coisa interessante'
#lista_palavra = frase.split()
lista_frase = frase.split(',')

lista_frases_arrumado = []

for i, frase in enumerate(lista_frase):
    lista_frases_arrumado.append(lista_frase[i].strip())

# print(lista_frases_arrumado)
# print(lista_frase)

frase_unida = '-'.join(lista_frases_arrumado)
print(frase_unida)
