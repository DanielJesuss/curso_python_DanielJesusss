"""
Peça ao usuário para digitar uma palavra.
Usando while, conte quantas vogais existem nessa palavra.
Ao final, exiba: "A palavra contém X vogais."
"""
palavra = input('Digite uma palavra: ')

i = 0
vogais = 0

while i < len(palavra):
    if palavra[i] in 'aeiouAEIOU':
        vogais += 1
    i += 1

print(f'A palavra contem {vogais} vogais.')
