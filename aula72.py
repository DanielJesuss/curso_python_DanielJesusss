# Exercicios com funções
"""
crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variavel e mostre o valor 
da variavel
"""
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(multiplicacao)

"""
crie uma função que fala se um numero é impar ou par
retorne se o valor é par ou impar
"""

def parimpar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par' 
    return f'{numero} é impar' 
    
print(parimpar(2))
print(parimpar(2))
print(parimpar(6))
print(parimpar(9))
print(parimpar(15))