"""
Desafio 058

Problema: Melhore o jogo do desafio 028 onde o computador vai "pensar" em um
          número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
          acertar, mostrando no final quantos palpites foram necessários para vencer.

Resolução do problemas:
"""
from random import randint
numeroSorteado = randint(0, 10)

chuteJogador = -1
qtdTentativas = 0

print('Olá, eu sou o J.A.R.V.I.S\nVamos ver se você consegue acertar essa.')
while chuteJogador != numeroSorteado:
    chuteJogador = int(input('\nChute um valor númerico entre 0 e 10: '))
    if chuteJogador != numeroSorteado:
        if chuteJogador < numeroSorteado:
            print('Errouuu kkkk. É MAIS que isso, humano!')
        if chuteJogador > numeroSorteado:
            print('Errouuu kkkk. É MENOS que isso, humano!')

    qtdTentativas += 1

print('\nParabéns humano, você acertou o valor que escolhi.')
print('Você tentou {} vezes até acertar.'.format(qtdTentativas))
