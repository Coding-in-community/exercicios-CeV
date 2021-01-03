=begin
Desafio 012

Problema: Faça um algoritmo que leia o preço de um produto e
          mostre seu novo preço, com 5% de desconto.

Resolução do problema:
=end

print"Digite o valor do produto: "
n = gets.chomp.to_f

desconto = (n*0.05)
puts"O produto com 5% de desconto fica #{desconto}."