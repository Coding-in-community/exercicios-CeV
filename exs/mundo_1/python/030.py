"""
Desafio 030

Problema:  Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

Resolução do problema:
"""
numero = int(input('Informe um número: '))
print('O número {} é PAR'.format(numero) if numero % 2 == 0 else 'O número {} é ÍMPAR.'.format(numero))
