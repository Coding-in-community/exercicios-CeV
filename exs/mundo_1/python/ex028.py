"""
Desafio 028

Problema: Escreva um programa que faça o computador "pensar"
          em um número inteiro entre 0 e 5 e peça para o usuário
          tentar descobrir qual foi o número escolhido pelo computador.
          O programa deverá escrever na tela se o usuário venceu ou perdeu.

Resolução do problema:
"""
from random import randint
maquina = randint(0, 5)

chute = int(input('Adivinhe o número um número entre 0 e 5: '))

if chute == maquina:
    print('Você ACERTOU.')
else:
    print('Você ERROU.')
    print('O número era {}'.format(maquina))
