"""
Introdução as funções (def) em python
Funções são trechos de codigo usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções python retornam none (nada)
"""


# def python(a, b, c):
#     print('Dentro da função')
#     print('Dentro da função')
#     print('Dentro da função')
#     print('Dentro da função')

# python()

# def imprimir(a, b, c):
#     print(a, b, c)

# imprimir(1, 2, 3)
# imprimir(4, 5, 6)


def saudacao(nome='Sem nome'):
    print('Olá, {nome}')

saudacao('Daniel')
saudacao('MAria')
saudacao('João')