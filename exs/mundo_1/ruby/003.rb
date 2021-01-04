=begin
Desafio 003

Problema: Crie um programa que leia dois números e mostre a soma entre eles.

Resolução do problema:
=end



print"Digite um número: "
n1 = gets.chomp.to_i

print"Digite outro número: "
n2 = gets.chomp.to_i

soma = n1 + n2
puts"a soma entre #{n1} e #{n2} é igual a #{soma}!"