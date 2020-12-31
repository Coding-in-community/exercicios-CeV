"""
Desafio 050

Problema: Desenvolva um programa que leia seis
          números inteiros e mostre a soma apenas
          daqueles que forem pares. Se o valor for
          ímpar, desconcidere-o.

Resolução do problema:
"""
somador = 0
for c in range(0, 6):
    numero = int(input('Informe um valor: '))
    if numero % 2 == 0:
        somador += numero
print('A soma de todos os valores pares informados é {}'.format(somador))
