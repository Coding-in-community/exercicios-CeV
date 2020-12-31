"""
Desafio 018

Problema: Faça um programa que leia um ângulo qualquer e mostre na
          tela o valor do seno, cosseno e tangente desse ângulo.

Resolução do problema:
"""
from math import radians, sin, cos, tan
angulo = int(input('Informe o angulo: '))

ang_radiano = radians(angulo)
seno = sin(ang_radiano)
cosseno = cos(ang_radiano)
tangente = tan(ang_radiano)

print('Seno: {:.4f}'.format(seno))
print('Cosseno: {:.4f}'.format(cosseno))
print('Tangente: {:.4f}'.format(tangente))
