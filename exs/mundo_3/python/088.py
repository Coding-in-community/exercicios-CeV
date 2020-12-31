"""
Desafio 088

Problema: Faça um programa que ajude um jogador da mega sena a criar palpites.
          O programa vai perguntar quantos jogos serão gerados e vai sortear
          6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
          composta.

Resolução do problema:
"""
from random import randint
from time import sleep

palpitesMega = []

print('=' * 35 + f'\n{"PALPITE MEGA SENA":^35}\n' + '=' * 35)

qtdJogos = int(input('Quantos jogos deseja: '))

print(f'\n{" > SORTEANDO VALORES < ":~^35}')
print()

for contagem in range(qtdJogos):
    jogo = []
    for qtdValores in range(6):
        sorteio = randint(1, 60)

        if sorteio in jogo:
            sorteio = randint(1, 60)
            jogo.append(sorteio)
        else:
            jogo.append(sorteio)

    jogo.sort()
    palpitesMega.append(jogo[:])
    print(f'Jogo {contagem + 1}: {palpitesMega[contagem]}')
    sleep(0.5)

print()
print(f'{" > BOA SORTE < ":~^35}')
