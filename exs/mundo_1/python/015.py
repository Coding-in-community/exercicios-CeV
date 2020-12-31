"""
Desafio 015

Problema: Escreva um programa que pergunte a quantidade de Km
          percorridos por um carro alugado e a quantidade de dias
          pelos quais ele foi alugado. Calcule o preço a pagar,
          sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

Resolução do problema:
"""
dia = int(input('Dias alugado: '))
km = int(input('Km rodados: '))

valor = (dia * 60) + (km * 0.15)

print('Total a pagar: R${:.2f}'.format(valor))
