"""
Desafio 063

Problema: Escreva um programa que leia um número N inteiro qualquer
          e mostre na tela os N primeiros elementos de uma sequência de Fibonacci.

          Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

Resolução do problema:
"""
n = int(input('Quantos elementos da sequência de Fibonacci deseja ver: '))

cont = fib1 = 0
fib2 = 1

while cont < n:
    print('{} -> '.format(fib1), end='')

    fib1, fib2 = fib2, fib1 + fib2

    cont += 1

print('FIM DA SEQUÊNCiA DE FIBONACCI.')
