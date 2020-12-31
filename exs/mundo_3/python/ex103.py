"""
Desafio 103

Problema: Faça um programa que tenha uma função chamada ficha(), que receba
          dois parâmetros opcionais: o nome de um jogador e quantos gols ele
          marcou.
          O programa deverá ser capaz de mostrar a ficha do jogador, mesmo
          que algum dado não tenha sido informado corretamente.

Resolução do problema:
"""


# Realiza a impressão da ficha do jogador
def ficha(nome_jogador='<desconhecido>', qtd_gols=0):
    print(f'O jogador {nome_jogador} fez {qtd_gols} gol(s) no campeonato.')


nome = input('Nome do jogador: ').strip().capitalize()
gols = input('Quantidade de gols: ').strip()
gols = int(gols) if gols.isnumeric() else 0

ficha(qtd_gols=gols) if nome == '' else ficha(nome, gols)
