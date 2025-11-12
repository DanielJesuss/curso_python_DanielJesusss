"""
Escreva um programa que retorna o valor hora
de um funcionario com base no seu salario mensal
e horas trabalhadas por mes
"""

# Solução 1

salario = int(input('Digite seu salario: '))
horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas: '))

valor_hora = salario / horas_trabalhadas

print(f'O valor da sua hora trabalhada é de {valor_hora}')