=begin
Desafio 010

Problema: Crie um programa que leia quanto dinheiro uma pessoa tem
          na carteira e mostre quantos dólares ela pode comprar.

Resolução do problema:
=end

print"Quantos Reais você tem? "
n = gets.chomp.to_f
dolar = 0.19 #preço do dolar no dia 4/1/2021
puts"Com esse dinheiro, você consegue comprar #{n*dolar}US$."