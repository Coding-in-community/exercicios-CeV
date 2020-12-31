"""
Desafio 033

Problema: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

Resolução do problema:
"""
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

maior = num1
menor = num1

# Maior
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

# Menor
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print('O número {} é o MAIOR'.format(maior))
print('O número {} é o MENOR'.format(menor))
