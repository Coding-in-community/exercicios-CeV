"""
Desafio 095

Problema: Aprimore o desafio 093 para que ele funcione com vários jogadores,
          incluindo um sistema de visualização de detalhes do aproveitamento
          de cada jogador.

Resolução do problema:
"""
jogador = dict()
totGols = 0
dadosTime = list()

# Para realizar cadastro de jogadores e seu desempenho nas partidas
while True:
    jogador['nome'] = input('Nome do jogador: ').strip().capitalize()
    qtdPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    print()

    jogador['gols'] = []  # Adicionando lista de gols na ficha do jogador

    # Adicionando gols
    for partida in range(qtdPartidas):
        jogador['gols'].append(int(input(f'Gols da {partida + 1}º partida: ')))
        totGols += jogador['gols'][partida]

    # Adicionando o total de gols feitos na ficha do jogador
    jogador['total'] = totGols
    totGols = 0
    dadosTime.append(jogador.copy())  # Inserindo dados dos jogadores nos dados do time

    print('-' * 60)
    continuar = input('Cadastrar novos dados? [S/N]: ').strip().upper()

    # Caso informe uma opção inválida entrará em loop até que seja válida
    while continuar not in ('S', 'N'):
        print('\nInforme a alternativa corretamente...')
        continuar = input('Cadastrar novos dados? [S/N]: ').strip().upper()
    print('-' * 60)

    # Finaliza cadastros de dados de jogadores
    if continuar == 'N':
        break

# Estrutura da tabela para análise
print(f'\n{"ID":^3}{"NOME":<20}{"GOLS":<20}{"TOTAL":<5}')
print('-' * 60)
for cod, infoJogador in enumerate(dadosTime):
    print(f'{cod:^3}', end='')
    for valor in infoJogador.values():
        print(f'{str(valor):<20}', end='')
    print()

print('-' * 60)

# Para escolher jogador pelo id e visualizar seu desempenho nas partidas
while True:
    visualizar = int(input('Digite o ID para visualizar ou 999 para sair: '))

    # Em caso de informar o ID inválido entrará em loop até que seja informado um válido
    while visualizar < 0 or visualizar > len(dadosTime) - 1 and visualizar != 999:
        print(f'\nERRO! Não existe jogador com o ID {visualizar}')
        visualizar = int(input('Digite o ID para visualizar ou 999 para sair: '))

    # Finaliza o programa
    if visualizar == 999:
        print('\n---- ANÁLISE FINALIZADA ----')
        break

    # Informa o desempenho do jogador escolhido
    print(f'\nLEVANTAMENTO DO JOGADOR --> {dadosTime[visualizar]["nome"]}')
    for partida, gol in enumerate(dadosTime[visualizar]['gols']):
        print(f'\t--> Na {partida + 1}º partida, fez {gol} gols.')
    print('-' * 60)
