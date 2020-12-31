"""
Desafio 036

Problema: Escreva um programa para aprovar o empréstimo bancário para a
          compra de uma casa. Pergunte o valor da casa, o salário do comprador
          e em quantos anos ele vai pagar. A prestação mensal não pode exceder
          30% do salário ou então o empréstimo será negado.

Resolução do problema:
"""
valor_casa = float(input('Informe o valor da casa: R$'))
salario_comprador = float(input('Informe o sálario do comprador: R$'))
quantidade_anos = int(input('Anos de financiamento: '))

prestacao = valor_casa / (quantidade_anos * 12)

if prestacao < salario_comprador * 30 / 100:
    print('FINANCIAMENTO ACEITO!!!\nA prestação será de R${:.2f}/Mês durante {} Anos.'.format(prestacao, quantidade_anos))
else:
    print('FINANCIAMENTO NEGADO!!!\nSALÁRIO INSUFICIENTE.')
