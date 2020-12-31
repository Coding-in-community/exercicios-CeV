"""
Desafio 016

Problema: Crie um programa que leia um número Real qualquer
          pelo teclado e mostre na tela a sua porção Inteira.

Resolução do problema:
"""
import math

num = float(input('Informe um número flutuante: '))
print(math.trunc(num))  # Metodo floor() tem o mesmo resultado
