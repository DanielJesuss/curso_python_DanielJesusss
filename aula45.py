"""
Iterável -> str, range, etc
Iterador -> quem sabe entrear um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
texto = 'Daniel'
iterador = iter(texto)

while True:
    try:
        letra = (next(iterador))
        print(letra)
    except StopIteration:
        break
