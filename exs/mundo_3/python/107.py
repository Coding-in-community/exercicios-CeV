"""
Desafio 107

Problema: Crie um módulo chamado moedas.py que tenha as funções incorporadas
          aumentar(), diminuir(), dobro() e metade().

          Faça também um programa que importe esse módulo e use algumas dessas
          funçóes.

Resolução do problema:
"""
from ex107_modulo import moeda

valor = float(input('Informe um valor: R$'))

print(f'Aumento de 10%: {moeda.aumentar(valor, 10):.2f}')
print(f'Rezudino 15 %: {moeda.diminuir(valor, 15):.2f}')
print(f'O dobro de {valor:.2f} é: {moeda.dobro(valor):.2f}')
print(f'A metade de {valor:.2f} é: {moeda.metade(valor):.2f}')
