"""
Desafio 037

Problema: Escreva um programa em Python que leia um número
          inteiro qualquer e peça para o usuário escolher qual
          será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

Resolução do problema:
"""
numero = int(input('Informe um número: '))
print('=-' * 10)
print('[ 1 ] BINÁRIO \n[ 2 ] OCTAL \n[ 3 ] HEXADECIMAL')
print('=-' * 10)

op = int(input('Escolha uma opção: '))
if op == 1:
    print('O valor {} convertido para BINÁRIO É: {}.'.format(numero, bin(numero)[2:]))
elif op == 2:
    print('O valor {} convertido para OCTAL É: {}.'.format(numero, oct(numero)[2:]))
elif op == 3:
    print('O valor {} convertido para HEXADECIMAL É: {}.'.format(numero, hex(numero)[2:]))
else:
    print('Opção INVÁLIDA.')
