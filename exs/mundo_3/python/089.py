"""
Desafio 089

Problema: Crie um programa que leia nome e duas notas de vários alunos
          e guarde tudo em uma lista composta. No final, mostre um
          boletim contendo a média de cada um e permita que o usuário
          possa mostrar as notas de cada aluno individualmente.

Resolução do problema:
"""
historicoAlunos = []
dadosAluno = []

while True:
    dadosAluno.append(input('NOME: ').strip().capitalize())
    dadosAluno.append([float(input('NOTA 1: ')), float(input('NOTA 2: '))])

    # Notas menores que 0 e maiores que 10 são inválidas, então solicida novamente em caso verdaidero
    while (dadosAluno[1][0] < 0 or dadosAluno[1][0] > 10) or (dadosAluno[1][1] < 0 or dadosAluno[1][1] > 10):
        print('-' * 25)
        print('Nota inválida, informe notas de 0 a 10...')
        dadosAluno[1].clear()  # Limpa dados inválidos

        print(f'NOME: {dadosAluno[0]}')
        dadosAluno[1].append(float(input('NOTA 1: ')))
        dadosAluno[1].append(float(input('NOTA 2: ')))

    historicoAlunos.append(dadosAluno[:])  # Cópia completa
    dadosAluno.clear()  # Limpando lista de dados
    print('-' * 25)

    continuar = input('Continuar [S/N]: ').strip().upper()

    # Caso informa uma opção inválida, entrará em loop até que informe uma valida
    while continuar not in ('S', 'N'):
        print('\nInforme a opção corretamente...')
        continuar = input('Continuar [S/N]: ').strip().upper()
    print('-' * 25)

    if continuar == 'N':
        print('\n')
        print('+------------------------------+' + f'\n|{"MÉDIAS":^30}|\n' + '+-----+----------------+-------+')
        break

for idx, nome in enumerate(historicoAlunos):
    if idx == 0:
        # Formatando cabeçalho da tabela
        print(f'| {"ID":<4}| {"NOME":<15}| {"MÉDIA":<6}|\n' + '+-----+----------------+-------+')

    media = (historicoAlunos[idx][1][0] + historicoAlunos[idx][1][1]) / 2
    print(f'| {idx:<4}| {historicoAlunos[idx][0]:<15}| {media:<6.1f}|')  # Dados da tabela
    print('+-----+----------------+-------+')

while True:
    id_aluno = int(input('\nID DO ALUNO ou (999 para sair): '))

    while 0 > id_aluno or id_aluno > len(historicoAlunos) - 1 and id_aluno != 999:
        print('~' * 37)
        print('\nInforme um ID correto...')
        id_aluno = int(input('ID DO ALUNO ou (999 para sair): '))
    print('-' * 37)

    if id_aluno == 999:
        print('\nPrograma finalizado...')
        break

    print(f'Aluno(a): {historicoAlunos[id_aluno][0]}\nNotas: {historicoAlunos[id_aluno][1]}')
    print('-' * 37)
