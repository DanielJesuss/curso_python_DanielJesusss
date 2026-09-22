"""
Crie funções que duplicam, triplicam e quadriplicam 
o numero recebido como parametro
"""
# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

# print(duplicar(2))
# print(triplicar(2))
# print(quadruplicar(2))

def criar_multiplicadores(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicadores(2)
triplicar = criar_multiplicadores(3)
quadruplicar = criar_multiplicadores(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))