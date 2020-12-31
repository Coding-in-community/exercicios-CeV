"""
Desafio 039

Problema: Faça um programa que leia o ano de nascimento de um jovem e informe,
          de acordo com a sua idade, se ele ainda vai se alistar ao serviço
          militar, se é a hora exata de se alistar ou se já passou do tempo
          do alistamento. Seu programa também deverá mostrar o tempo que falta
          ou que passou do prazo.

Resolução do problema:
"""
from datetime import date
ano_nasc = int(input('Informe o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade < 18:
    print('Ainda vai se ALISTAR.')
    print('Você vai se ALISTAR daqui {} ano(s), em {}'.format(18 - idade, ano_atual + (18 - idade)))
elif idade == 18:
    print('Está na hora de se ALISTAR.')
else:
    print('Passou da hora de se ALISTAR')
    print('Você deveria ter se ALISTADO há {} ano(s), em {}.'.format(idade - 18, ano_atual - (idade - 18)))
