"""
Interando strigs com while
"""
#       01234567891011
nome = 'Daniel Jesus' # Iteravel
#   -121110987654321


indice = 0
resultado = ''

while indice < len(nome):
    resultado += nome[indice] + ' '
    indice += 1

print(resultado)


