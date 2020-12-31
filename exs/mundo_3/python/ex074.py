"""
Desafio 074

Problema: Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
          Depois disso, mostre a listagem de números gerados e também indique o menor e
          o maior valor que estão na tupla.

Resolução do problema:
"""
from random import randint
print('-' * 30 + f'\n{"SORTEIO DE VALORES": ^30}\n' + '-' * 30)

# Atribuindo valores sorteados a uma tupla
valorSorteado = ()
for cont in range(0, 5):
    valorSorteado += randint(1, 10),  # Pode-se utilizar uma

# Listando valores sorteados formatados sem Aspas e Parênteses
print('Valores Sorteados: ', end='')
for idx, valor in enumerate(valorSorteado):
    print(f'{valorSorteado[idx]}', end=' ')

print(f'\nMAIOR VALOR: {max(valorSorteado)}\nMENOR VALOR: {min(valorSorteado)}')
