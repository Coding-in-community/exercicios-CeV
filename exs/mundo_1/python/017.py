"""
Desafio 017

Problema: Faça um programa que leia o comprimento do cateto oposto e
          do cateto adjacente de um triângulo retângulo. Calcule e
          mostre o comprimento da hipotenusa.

Resolução do problema:
"""
from math import hypot
cateto_oposto = int(input('Informe o cateto oposto: '))
cateto_adjacente = int(input('Informe o cateto adjacente: '))

hipostenusa = hypot(cateto_oposto, cateto_adjacente)  # H² = C² + C² // H² = (C² + C²) ** (1/2)
print('Hipotenusa: {:.2f}'.format(hipostenusa))

