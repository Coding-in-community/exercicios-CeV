"""
Desafio 041

Problema: A Confederação Nacional de Natação precisa de um programa
          que leia o ano de nascimento de um atleta e mostre sua
          categoria, de acordo com a idade:
            - Até 9 anos: MIRIM
            - Até 14 anos: INFANTIL
            - Até 19 anos: JÚNIOR
            - Até 25 anos: SÊNIOR
            - Acima de 25 anos: MASTER

Resolução do problema:
"""
from datetime import date

ano = int(input('Informe o ano do seu nascimento: '))

idade = date.today().year - ano

if 0 < idade <= 9:
    print('O atleta tem {} anos, então está categoria MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos, então está categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos, então está categoria JUNIOR'.format(idade))
elif idade <= 20:
    print('O atleta tem {} anos, então está categoria SÊNIOR'.format(idade))
elif 20 < idade <= 100:
    print('O atleta tem {} anos, então está categoria MASTER'.format(idade))
else:
    print('Erro, idade INVÁLIDA, tente novamente.')
