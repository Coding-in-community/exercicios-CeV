"""
Desafio 070

Problema: Crie um programa que leia o nome e o preço de vários produtos.
          O programa deverá perguntar se o usuário vai continuar.
          No final, mostre:
            A) Qual é o total gasto na compra;
            B) Quantos produtos custam mais de R$1000;
            C) Qual é o nome do produto mais barato.

Resolução do problema:
"""
totalGasto, qtdProduto_maiorMilReais, precoProduto_maisBarato = 0, 0, 0
nomeProduto_maisBarato = ''

print('=' * 30 + f'\n{" AMAZON ":-^30}\n' + '=' * 30)

contador = 1  # Contador para saber quantas repetições de compra

while True:
    nomeProduto = input('NOME: ').strip().capitalize()
    precoProduto = float(input('PREÇO: R$'))

    # Verificação para nota fiscal
    totalGasto += precoProduto

    if precoProduto > 1000:
        qtdProduto_maiorMilReais += 1

    if contador == 1 or precoProduto < precoProduto_maisBarato:
        nomeProduto_maisBarato = nomeProduto
        precoProduto_maisBarato = precoProduto


    continuar = input('Novo Produtos ? [S/N]: ').strip().upper()

    while continuar != 'N' and continuar != 'S':
        print('Informe a opção CORRETAMENTE.')
        continuar = input('Novo Produtos ? [S/N]: ').strip().upper()

    if continuar == 'N':
        print('\nCOMPRA FINALIZADA. . .\n')
        break
    print('-' * 30)

    contador += 1

print('-' * 53 + f'\n{" NOTA FISCAL ":~^53}\n' + '-' * 53)
print(f'TOTAL: R${totalGasto:.2f}')
print(f'VOCÊ COMPROU {qtdProduto_maiorMilReais} PRODUTOS COM PREÇO MAIOR QUE R$1000.00')
print(f'PRODUTO MAIS BARATO: {nomeProduto_maisBarato}, PREÇO: R${precoProduto_maisBarato:.2f}')
