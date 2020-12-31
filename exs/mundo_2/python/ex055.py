"""
Desafio 055

Problema: Faça um programa que leia o peso de cinco pessoas.
          No final, mostre qual foi o maior e o menor peso lidos.

Resolução do problemas:
"""
maiorPeso = 0.0
menorPeso = 0.0

for c in range(5):
    peso = float(input('Informe o peso da {}º pessoa: '.format(c + 1)))

    if c == 0:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso

        if peso < menorPeso:
            menorPeso = peso

print('O maior peso é de {}Kg\nE o menor peso é de {}Kg'.format(maiorPeso, menorPeso))
