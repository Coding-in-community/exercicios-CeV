"""
Desafio 092

Problema: Crie um programa que leia nome, ano de nascimento e carteira de trabalho de uma pessoa e
          cadastre-os (com idade) em um dicionário se por acaso a CTPS (Carteira de Trabalho e Previdência Social)
          for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
          Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

Resolução do problema:
"""
from datetime import date
dados = dict()

dados['nome'] = input('NOME: ').strip().capitalize()
dados['idade'] = date.today().year - int(input('DATA NASCIMENTO: '))
dados['ctps'] = int(input('Nº CARTEIRA DE TRABALHO (0 se não tem): '))

# Caso possua CTPS
if dados['ctps'] > 0:
    dados['contratação'] = int(input('ANO DE CONTRATAÇÃO: '))
    dados['salário'] = float(input('SALÁRIO: R$'))
    dados['aposentadoria'] = dados['contratação'] - (date.today().year - dados['idade']) + 35

# Mostrando os dados pessoais na tela
print()
print('-' * 25 + f'\n{"DADOS PESSOAIS":^25}\n' + '-' * 25)
for chave, valor in dados.items():
    print(f'{chave}: {valor}')
