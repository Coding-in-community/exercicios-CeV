=begin
Desafio 036

Problema: Escreva um programa para aprovar o empréstimo bancário para a
          compra de uma casa. Pergunte o valor da casa, o salário do comprador
          e em quantos anos ele vai pagar. A prestação mensal não pode exceder
          30% do salário ou então o empréstimo será negado.

Resolução do problema:
=end

print"Informe o valor da casa: "
valorCasa = gets.chomp.to_f

print"Informe o sálario do comprador: "
salario = gets.chomp.to_f

print"Informe a quantidade de anos de financiamento: "
anos = gets.chomp.to_i

prestacao = valorCasa /(anos * 12)

if prestacao < salario * 1.30
	puts"FINANCIAMENTO ACEITO!!\nA prestação será de R$#{prestacao}/Mês durante #{anos} anos."
else
	puts"FINANCIAMENTO RECUSADO!! Sálario muito baixo para fazer o financiamento."
end

