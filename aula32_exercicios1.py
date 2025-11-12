"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_digitado = int(input('Digite um número: '))
resto = 0

if numero_digitado % 2 == resto:
    print('Este número é par')
elif numero_digitado % 2 != resto:
    print('Este número é impar')
