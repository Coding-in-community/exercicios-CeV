"""
Desafio 004

Problema: Faça um programa que leia algo pelo teclado e mostre na tela
          seu tipo primitivo e todas as informações possíveis sobre ela.

Resolução do problema:
"""
valor = input('Digite algo: ')
print('O tipo primitivo desse valor é \033[31m{}\033[m'.format(type(valor)))
print('É um número ? \033[34m{}\033[m'.format(valor.isnumeric()))
print('É um digito ? \033[30m{}\033[m'.format(valor.isdigit()))
print('É um valor alpha-númerico \033[35m{}\033[m?'.format(valor.isalnum()))
print('É texto ? \033[33m{}\033[m'.format(valor.isalpha()))
print('É um valor decimal ? \033[32m{}\033[m'.format(valor.isdecimal()))
print('É um identiicador ? \033[35m{}\033[m'.format(valor.isidentifier()))
print('Está em letra minúscula ? \033[37m{}\033[m'.format(valor.islower()))
print('Está em lestra maiúscula ? \033[36m{}\033[m'.format(valor.isupper()))
print('É uma tabela de impressão ? \033[34m{}\033[m'.format(valor.isprintable()))
print('É um espaço ? \033[31m{}\033[m'.format(valor.isspace()))
print('É um capitalizada ? \033[30m{}\033[m'.format(valor.istitle()))
