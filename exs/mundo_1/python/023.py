"""
Desafio 023

Problema: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Resolução do problema:
"""
numero = input('Informe o número: ')
# print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(numero[-1], numero[-2], numero[-3], numero[0]))
# print()

numero = int(numero)
# mi = (numero // 1000) * 1000
# ce = ((numero - mi) // 100) * 100
# de = ((numero - mi - ce) // 10) * 10
# uni = numero - mi - ce - de

uni = numero // 1 % 10
de = numero // 10 % 10
ce = numero // 100 % 10
mi = numero // 1000 % 10
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(uni, de, ce, mi))
