"""
Desafio 029

Problema: Escreva um programa que leia a velocidade de um carro.
          Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
          que ele foi multado. A multa vai custar R$7,00 por cada
          Km acima do limite.

Resolução do problema:
"""
velocidade = int(input('Informe a velocidade do carro: '))

if velocidade > 80:
    print('Você foi multado.')
    multa = (velocidade - 80) * 7.00
    print('Você vai pagar R$ {:.2f} de multa.'.format(multa))
