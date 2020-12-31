"""
Desafio 093

Problema: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
          O programa vai ler o nome do jogador e quantas partidas ele jogou.
          Depois vai ler a quantidade de gols feitos em cada partida.
          No final, tudo isso será guardado em um dicionário, incluindo o total de gols
          feitos durante o campeonato.

Resolução do problema:
"""
jogador = dict()

jogador['nome'] = input('Nome do jogador: ').strip().capitalize()
qtdPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
print()

jogador['gols'] = []  # Adicionando lista de gols na ficha do jogador
totGols = 0

# Adicionando gols
for partida in range(qtdPartidas):
    jogador['gols'].append(int(input(f'\tGols da {partida + 1}º partida: ')))
    totGols += jogador['gols'][partida]

# Adicionando o total de gols feitos na ficha do jogador
jogador['total'] = totGols

# Dicionário completo
print()
print('-' * 60)
print(jogador)
print('-' * 60)

# Campos e seus dados
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}.')
print()

# Mostrando gols por partida
print(f'O jogador {jogador["nome"]} jogou {qtdPartidas} partidas.')
for partida, gol in enumerate(jogador['gols']):
    print(f'\t--> Na {partida + 1}º, fez {gol} gols.')
print(f'Foi um total de {jogador["total"]}')
