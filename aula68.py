"""
Escopo de funções em Python
Escopo significa o local onde aquele codigo pode atingir
Existe escopo global e local
O escopo global é onde todo o codigo é alcançavel
O escopo local é onde apenas nomes do mesmo local podem 
ser alcançados
"""
x = 1


def escopo():
    global x 
    x = 10

    def outra_funcao():
        x = 1
        y = 2
        print(x, y)    
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)