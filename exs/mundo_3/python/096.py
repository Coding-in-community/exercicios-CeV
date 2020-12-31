"""
Desafio 096

Problema: Faça um programa que tenha uma função chamada area(), que receba as dimeções
          de um terreno retangular(largura e comprimento) e mostre a área do terreno.

Resolução do problema:
"""


# Função para impressão de cabeçalho
def header(mensagem):
    print('-' * 30)
    print(f'{mensagem:^30}')
    print('-' * 30)


# Função para calcular area do terreno
def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno de {largura}x{comprimento} é de {area}m²')


header('Área de Terreno')
larg = float(input('Largura em (m): '))
compri = float(input('Comprimento em (m): '))

area(larg, compri)
