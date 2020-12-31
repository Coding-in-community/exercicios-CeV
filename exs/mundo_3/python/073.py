"""
Desafio 073

Problema: Crie uma tupla preenchida com os 20 primeiros colocados da tabela do
          Campeonato Brasileiro de Futebol, na ordem de colocação.

          Depois mostre:
            A) Apenas mostre os 5 primeiros colocados;
            B) Os últimos 4 colocados da tabela;
            C) Uma lista com os times em ordem alfabética;
            D) Em que posição da tabela está o time da Chapecoense.

Resolução do problema:
"""
tabelaBrasileiro = ('Palmeiras', 'Atlético', 'São Paulo', 'Santos', 'Internacional',
                    'Goiás', 'Botafogo', 'Corinthians', 'Flamengo', 'Athletico-PR',
                    'Bahia', 'Ceará SC', 'Fluminense', 'Fortaleza', 'Cruzeiro',
                    'Chapecoense', 'Avaí', 'CSA', 'Grêmio', 'Vasco da Gama')

print('-' * 30 + f'\n{"BRASILEIRÃO 2019": ^30}\n' + '-' * 30)

# Lista time e sua colocação na tabela da tabela
for idx, time in enumerate(tabelaBrasileiro):
    print(f'{idx + 1:>8}º - {time}')

print()
print('-' * 90 + f'\n{"DADOS": ^90}\n' + '-' * 90)

print(f'5 Primeiros colocados: {tabelaBrasileiro[0: 5]}')
print('-' * 90)
print(f'4 Últimos colocados: {tabelaBrasileiro[-4:]}')
print('-' * 90)
print(f'Times em Ordem Alfabética: {sorted(tabelaBrasileiro)}')
print('-' * 90)
print(f'Posição Chapecoense: {tabelaBrasileiro.index("Chapecoense") + 1}º Posição')
