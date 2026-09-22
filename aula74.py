"""
Closure e funções que retomam outras funções
"""
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bomdia = criar_saudacao('Bom dia')
falar_boanoite = criar_saudacao('Boa noite')

print(falar_bomdia('Daniel'))
print(falar_boanoite('Luiz'))