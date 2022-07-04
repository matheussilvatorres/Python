"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA."""

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('Você digitou a frase: {}'.format(junto))
# for letra in range(len(junto) - 1, -1, -1):
#     inverso += junto[letra]
print('O contrario da frase digitada é: {}'.format(inverso))
if inverso == junto:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')