#rie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGUEM', 'PYTHON', 'CURSO',
            'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
vogais = ('A', 'E', 'I', 'O', 'U')
for p in palavras:
    print(f'\nNa palavra {p.lower()} temos as vogais: ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
