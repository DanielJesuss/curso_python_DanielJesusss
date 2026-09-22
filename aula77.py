# Exercicio - Sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '5'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['41', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])

    lista_de_opcoes = pergunta['Opções']
    resposta_certa = pergunta['Resposta']

    print('Opções:')

    for i, opcao in enumerate(lista_de_opcoes):
        print(f'{i}) {opcao}')
    
    try:
        indice_escolhido = int(input('Escolha uma opção: '))

        if 0 <= indice_escolhido < len(lista_de_opcoes):
            valor_escolhido = lista_de_opcoes[indice_escolhido]

            if valor_escolhido == resposta_certa:
                print('Parabens, resposta correta!! 👌👍')
                acertos += 1
            else: 
                print('Putz, resposta errada!! ❌😢')
        else:
            print('❌ Erro: Essa opção não existe. Resposta considerada errada.')
            
    except ValueError:
        print('❌ Erro: Você deve digitar um número. Resposta considerada errada.')

print('---')
print(f'Voce acertou: {acertos} vezes')
print('---')