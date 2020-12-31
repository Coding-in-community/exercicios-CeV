"""
Desafio 044

Problema: Elabore um programa que calcule o valor a ser pago
          por um produto, considerando o seu preço normal e
          condição de pagamento:
            - à vista dinheiro/cheque: 10% de desconto
            - à vista no cartão: 5% de desconto
            - em até 2x no cartão: preço formal
            - 3x ou mais no cartão: 20% de juros

Resolução do problema:
"""
preco_produto = float(input('Informe o preço do produto: R$'))
print()
print('''FORMAS DE PAGAMENTO
[1] À vista no dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
print()
condicao_pagamento = int(input('Informe a forma de pagamento: '))
if condicao_pagamento == 1:
    valor_total = preco_produto - (preco_produto * 10 / 100)
    print('TOTAL A PAGAR COM 10% DE DESCONTO:  R${:.2f} '.format(valor_total))
elif condicao_pagamento == 2:
    valor_total = preco_produto - (preco_produto * 5 / 100)
    print('TOTAL A PAGAR COM 5% DE DESCONTO: R${:.2f}'.format(valor_total))
elif condicao_pagamento == 3:
    valor_total = preco_produto
    parcelas_mensal = valor_total / 2
    print('TOTAL A PAGAR: R${:.2f}, SENDO 2x R${:.2f}/MÊS'.format(valor_total, parcelas_mensal))
elif condicao_pagamento == 4:
    valor_total = preco_produto + (preco_produto * 20 / 100)
    quant_parcelas = int(input('Informe quantas parcelas deseja pagar: '))
    parcelas_mensal = valor_total / quant_parcelas
    print('TOTAL A PAGAR: R${:.2f} COM JUROS, SENDO {}x de R${:.2f}/MÊS'.format(valor_total, quant_parcelas, parcelas_mensal))
else:
    print('ERRO, INFORME UMA FORMA DE PAGAMENTO VALIDA.')
