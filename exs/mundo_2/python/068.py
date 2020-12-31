"""
Desafio 068

Problema: Faça um programa que jogue PAR ou ÍMPAR com o computador.
          O jogo só será interrompido quando o jogador perder,
          mostrando o total de vitórias consecutivas que ele consquistou
          no fim do jogo.

Resolução do problema:
"""
from random import randint
print('-' * 30)
print(f'{" Par ou Ímpar ":~^30}')
print('-' * 30)

acumulador = 0
while True:
    jogador = int(input('\nInforme um valor: '))
    parOrImpar = input('Deseja PAR ou ÍMPAR ? [P/I] ').strip().upper()
    print('-' * 30)
    computador = randint(0, 10)

    while parOrImpar != 'P' and parOrImpar != 'I':
        print('Informe corretamente qual deseja.')
        parOrImpar = input('Deseja PAR ou ÍMPAR ? [P/I] ').strip().upper()
        print('-' * 30)

    resulValor = jogador + computador

    print(f'Você jogou: {jogador}\nComputador jogou: {computador}\n{jogador} + {computador} = {jogador + computador}')

    if resulValor % 2 == 0:
        print('Resultado: Deu PAR')
        if parOrImpar == 'P':
            print('\nVocê Acertou!!!')
            print('Mais uma rodada...')
            acumulador += 1
        else:
            print('\nVocê Perdeu!!!')
            break
    else:
        print('Resultado: Deu ÍMPAR')
        if parOrImpar == 'I':
            print('\nVocê Acertou!!!')
            print('Mais uma rodada...')
            acumulador += 1
        else:
            print('\nVocê Perdeu!!!')
            break
    print('-' * 30)

print('-' * 30)
print('FIM DE JOGO!!!')
print('-' * 30)
print(f'Você teve {acumulador} vitória(s) consecutiva(s)')
