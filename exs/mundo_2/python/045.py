"""
Desafio 045

Problema: Crie um programa que faça o computador jogar Jokenpô com você.

Resolução do problema:
"""
from random import randint  # Importanda da Lib random o modulo randint
lista_jogada = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)  # Sorteando número de 0 a 2

# Solicitando um valor e subtraindo 1 dele
jogador = int(input('[ 1 ] Pedra \n[ 2 ] Papel \n[ 3 ] Tesoura \nEscolha uma opção: ')) - 1

# Verificação da situação do jogo, ganhador/empate
if 0 <= jogador < 3:
    # 1 = Pedra; 2 = Papel; 3 = Tesoura
    print('Você \033[34m{}\033[m X \033[31m{}\033[m Computador'.format(lista_jogada[jogador], lista_jogada[computador]))

    #Empate
    if jogador == computador:
        print('\033[30mJOGO EMPATADO')

    # Jogador escolhendo Pedra
    elif jogador == 0 and computador == 1:
        print('\033[30mCOMPUTADOR GANHOU')
    elif jogador == 0 and computador == 2:
        print('\033[30mVOCÊ GANHOU')

    # Jogador Escolhendo Papel
    elif jogador == 1 and computador == 2:
        print('\033[30mCOMPUTADOR GANHOU')
    elif jogador == 1 and computador == 0:
        print('\033[30mVOCÊ GANHOU')

    # Jogador Escolhendo Tesoura
    elif jogador == 2 and computador == 0:
        print('\033[30mCOMPUTADOR GANHOU')
    elif jogador == 2 and computador == 1:
        print('\033[30mVOCÊ GANHOU')
else:
    print('\033[30;41mJOGADA INVALIDA, TENTE NOVAMENTE.\033[m')
