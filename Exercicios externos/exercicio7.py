"""
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite o 
usuário chute um numero até que o valor aleatrorio gerado no inicio do programa sea 
chutado corretamente

o programa deve informar se o chute foi alto ou baixo
"""

aleatorio = 6
chute = ''

while True:
    chute = int(input('Digite um numero (chute): '))

    if aleatorio == chute:
        print('Parabens você acertou!!!')
        break

    if chute > aleatorio:
        print('Você chutou alto')
    else:
        print('Você chutou baixo')
    continue