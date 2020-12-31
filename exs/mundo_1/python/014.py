"""
Desafio 014

Problema: Escreva um programa que converta uma temperatura
          digitando em graus Celsius e converta para graus Fahrenheit.

Resolução do problema:
"""
temperatura_C = float(input('Informe a temperatura em °C: '))

temperatura_F = 1.8 * temperatura_C + 32

print('Temperatura em: {:.1f}°F'.format(temperatura_F))
