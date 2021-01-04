=begin
Desafio 015

Problema: Escreva um programa que pergunte a quantidade de Km
          percorridos por um carro alugado e a quantidade de dias
          pelos quais ele foi alugado. Calcule o preço a pagar,
          sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

Resolução do problema:
=end

print"Quantos Km foram percorridos? "
km = gets.chomp.to_f

print"Por quantos dias o carro foi alugado? "
dias = gets.chomp.to_f

preco = (dias*60)+(km*0.15)

puts"O valor do aluguel é #{preco}R$."