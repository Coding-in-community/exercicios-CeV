=begin
Desafio 017

Problema: Faça um programa que leia o comprimento do cateto oposto e
          do cateto adjacente de um triângulo retângulo. Calcule e
          mostre o comprimento da hipotenusa.

Resolução do problema:
=end

print"Digite o valor do cateto oposto: "
co = gets.chomp.to_f

print"Digite o valor do cateto adjacente: "
ca = gets.chomp.to_f

h = ((co**2)+(ca**2))**0.5

puts"A hipotenusa vale #{h}."
