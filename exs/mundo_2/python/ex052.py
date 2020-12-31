"""
Desafio 052

Problema: Faça um programa que leia um número
          inteiro e diga se ele é ou não um número
          primo.

Resolução do problemas:
"""
numero = int(input('Informe um valor: '))
qtdDivisao = 0  # Quantidade de divisões realizadas

for c in range(1, numero + 1):

    if numero % c == 0:
        qtdDivisao += 1

print('O número informado foi dividido {} vezes'.format(qtdDivisao))
if qtdDivisao == 2:
    print('O valor informado é PRIMO')
else:
    print('O valor informado não é PRIMO')
