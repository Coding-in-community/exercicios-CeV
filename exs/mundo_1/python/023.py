"""
Desafio 023

Problema: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Resolução do problema:
"""
numero = input('Informe o número: ')

numero = int(numero)

uni = numero // 1 % 10
de = numero // 10 % 10
ce = numero // 100 % 10
mi = numero // 1000 % 10
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(uni, de, ce, mi))
