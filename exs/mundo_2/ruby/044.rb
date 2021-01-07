=begin
Desafio 044

Problema: Elabore um programa que calcule o valor a ser pago
          por um produto, considerando o seu preço normal e
          condição de pagamento:
            - à vista dinheiro/cheque: 10% de desconto
            - à vista no cartão: 5% de desconto
            - em até 2x no cartão: preço formal
            - 3x ou mais no cartão: 20% de juros

Resolução do problema:
=end
print'Informe o preço do produto: R$'
preco_produto = gets.chomp.to_f

puts '''FORMAS DE PAGAMENTO
[1] À vista no dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão'''

print"Informe a forma de pagamento: "
condicao_pagamento = gets.chomp.to_i
if condicao_pagamento == 1
    valor_total = preco_produto - (preco_produto * 0.10)
    puts"TOTAL A PAGAR COM #{"10%"} DE DESCONTO: R$#{valor_total.round(2)}." 

elsif condicao_pagamento == 2
    valor_total = preco_produto - (preco_produto * 0.05)
    puts"TOTAL A PAGAR COM #{"5%"} DE DESCONTO: R$#{valor_total.round(2)}."

elsif condicao_pagamento == 3
    valor_total = preco_produto
    parcelas_mensal = valor_total / 2
    puts"TOTAL A PAGAR: R$#{valor_total}, SENDO 2x R$#{parcelas_mensal.round(2)}/MÊS."

elsif condicao_pagamento == 4
    valor_total = preco_produto + (preco_produto * 0.20)
    print'Informe quantas parcelas deseja pagar: '
    quant_parcelas = gets.chomp.to_i
    parcelas_mensal = valor_total / quant_parcelas
    puts"TOTAL A PAGAR: R$#{valor_total} COM JUROS, SENDO #{quant_parcelas.round(2)}x de R$#{parcelas_mensal.round(2)}/MÊS."

else
    abort"ERRO, INFORME UMA FORMA DE PAGAMENTO VALIDA."
end
