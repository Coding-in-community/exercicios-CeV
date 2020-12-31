"""
Desafio 064

Problema: Crie um programa que leia vários números inteiros pelo teclado.
          O programa só vai parar quando o usuário digitar o valor 999,
          que é a condição de parada. No final, mostre quantos números
          foram digitados e qual foi a soma entre eles.
          Desconsiderando o flag(999).

Resolução do problema:
"""
num = contNum = acumulador = 0
while num != 999:
    contNum += 1
    acumulador += num
    num = int(input('Informe um valor ou 999 para sair: '))

print('\nForam informados {} números\nE a soma entre eles é {}'.format(contNum - 1, acumulador))
