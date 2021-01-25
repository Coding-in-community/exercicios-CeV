"""
Desafio 031

Problema: Desenvolva um programa que pergunte a distância de
          uma viagem em Km. Calcule o preço da passagem, cobrando
          R$0,50 por Km para viagens de até 200Km e R$0,45 para
          viagens mais longas.

Resolução do problema:
"""
distancia = int(input('Informe a distância em KM: '))

preco_passagem = distancia * 0.45 if distancia > 200 else distancia * 0.50
print('O valor da passagem será R$ {:.2f}'.format(preco_passagem))
