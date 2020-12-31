"""
Desafio 078

Problema: Faça um programa que leia 5 valores númericos e guarde em uma lista.
          No final, mostre qual foi o maior e o menor valor digitado e as suas
          respectivas posições na lista.

Resolução do problema:
"""
valores = [int(input(f'Informe o valor da posição {cont}º: ')) for cont in range(5)]
print('-' * 35)
print(f'VALORES INFORMADOS: {valores}')

print(f'\nO maior valor digitado foi: {max(valores)} nas posições: ', end='')
for indice, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{indice}...', end=' ')

print(f'\nO menor valor digitado foi: {min(valores)} nas posições: ', end='')
for indice, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{indice}...', end=' ')
