""" Calculadora com while """

# operador1 = int(input("Digite um numero"))


while True:
    numero1 = input("Digite um número: ")
    numero2 = input("Digite outro número: ")
    operador = input("Digite o operador (+-/*): ")

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero1)
        num_2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um dos números está inválidos')
        continue

####
    operadores_permitidos = '+-/*'

    if operador not in  operadores_permitidos:
        print('Õperador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

####
    print('Realizando sua conta. Confira o resultado abaixo:')
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)    

####
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
    