"""
Desafio 048

Problema: Faça um programa que calcule a soma entre todos os
          números ímpares que são múltiplos de três e que se
          encontram no intervalo de 1 até 500.

Resolução do problema:
"""
somador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        somador += c
print('A soma de todos os valores ímpares múltiplos de três é: {}'.format(somador))
