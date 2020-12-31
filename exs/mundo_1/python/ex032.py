"""
Desafio 032

Problema: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

Resolução do problema:
"""
from datetime import date
ano = int(input('Informe o ano: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO.'.format(ano))
else:
    print('O ano de {} NÃO é BISSEXTO.'.format(ano))
