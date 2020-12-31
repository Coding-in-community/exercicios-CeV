"""
Desafio 057

Problema: Faça um programa que leia o sexo de uma pessoa. Mas só aceite
          os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
          até ter um valor correto.

Resolução do problemas:
"""
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Informe o sexo da pessoa [M/F]: ').strip().upper()
    print()

    if sexo != 'M' and sexo != 'F':
        print('Sexo inválido, tente novamente.\n')

if sexo == 'M':
    print('Pessoa do sexo masculino({}) cadastrado'.format(sexo))
else:
    print('Pessoa do sexo feminino({}) cadastrada'.format(sexo))
