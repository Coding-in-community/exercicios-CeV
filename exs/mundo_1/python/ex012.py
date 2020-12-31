"""
Desafio 012

Problema: Faça um algoritmo que leia o preço de um produto e
          mostre seu novo preço, com 5% de desconto.

Resolução do problema:
"""
preco = float(input('Informe o preço do produto: R$'))

total = preco - (preco * 5 / 100)

print('Total à pagar com 5% de desconto: R${:.2f}'.format(total))
