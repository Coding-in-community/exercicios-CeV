"""
Desafio 008

Problema: Escreva um programa que leia um valor em metros e o
          exiba convertido em centímetros e milímetros.

Resolução do problema:
"""
metro = int(input('Informe o valor em metro(s): '))

centimetro = metro * 100
milimetro = metro * 1000

print(f'Centrimento: {centimetro}cm')
print(f'Milimetro {milimetro}mm')