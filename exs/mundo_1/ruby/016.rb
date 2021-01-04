=begin
Desafio 016

Problema: Crie um programa que leia um número Real qualquer
          pelo teclado e mostre na tela a sua porção Inteira.

Resolução do problema:
=end

print"Digite um número real: "
n = gets.chomp.to_f

inteiro = n.to_i
puts"A parte inteira de #{n} é #{inteiro}."