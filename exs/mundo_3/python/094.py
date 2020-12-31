"""
Desafio 094

Problema: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados
          de cada pessoa em um dicionário e todos os dicionários em uma lista.
          No final, mostre:
            A) Quantas pessoas foram cadastradas;
            B) A média de idade do grupo;
            C) Uma lista com todas as mulheres;
            D) Uma lista com todas as pessoas com idade acima da média.

Resolução do problema:
"""
dados = {}
pessoas = []
acumulaIdade = 0

while True:
    dados['nome'] = input('NOME: ').strip().capitalize()
    dados['sexo'] = input('SEXO [M/F]: ').strip().upper()

    # Em caso de alternativa incorreta
    while dados['sexo'] not in ('M', 'F'):
        print('\nInforme a opção corretamente...')
        dados['sexo'] = input('SEXO [M/F]: ').strip().upper()

    dados['idade'] = int(input('IDADE: '))
    acumulaIdade += dados['idade']

    # Salvando a cópia dos dados na lista de pessoas
    pessoas.append(dados.copy())

    print('-' * 30)
    continuar = input('Deseja continuar? [S/N]: ').strip().upper()

    # Em caso de opção incorreta
    while continuar not in ('S', 'N'):
        print('\nInforme a opção corretamente...')
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    print('-' * 30)

    # Finalizando a execução do programa
    if continuar == 'N':
        break

print(f'{" ESTATÍSTICAS ":^30}\n' + '-' * 30)
print(f'QUANTIDADE DE CADASTROS: {len(pessoas)}')

idadeMedia = acumulaIdade / len(pessoas)
print(f'\nMÉDIA DE IDADE: {idadeMedia:.1f} anos')

print('\nMULHERES CADASTRADAS:')
for cadastro in pessoas:
    if cadastro['sexo'] == 'F':
        print(f'\t--> {cadastro["nome"]}')

print('\nPESSOAS COM IDADE ACIMA DA IDADE MÉDIA:')
for cadastro in pessoas:
    if cadastro['idade'] >= idadeMedia:
        for chave, info in cadastro.items():
            print(f'\t{chave} -> {info}')
        print('-' * 30)

print('----- PROGRAMA ENCERRADO -----')
