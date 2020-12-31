"""
Desafio 054

Problema: Crie um programa que leia o ano de nascimento
          de sete pessoas. No final, mostre quantas pessoas
          ainda não atingiram a maioridade e quantas já são maiores.

Resolução do problemas:
"""
from datetime import date

maioresDeIdade = 0
menoresDeIdade = 0
for c in range(7):
    ano_nascimento = int(input('Informe o ano de nascimento da {}º pessoa: '.format(c + 1)))

    if (date.today().year - ano_nascimento) < 21:
        menoresDeIdade += 1
    else:
        maioresDeIdade += 1
print()
print('Tem {} pessoas menores de idade\nE {} pessoas maiores de idade.'.format(menoresDeIdade, maioresDeIdade))
