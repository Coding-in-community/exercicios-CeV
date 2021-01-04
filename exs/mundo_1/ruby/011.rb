=begin
Desafio 011

Problema: Faça um programa que leia a largura e a altura de uma
          parede em metros, calcule a sua área e a quantidade de
          tinta necessária para pintá-la, sabendo que cada litro
          de tinta pinta uma área de 2 metros quadrados.

Resolução do problema:
=end

print"Qual a altura da parede? "
h = gets.chomp.to_f

print"Qual a largura da parede? "
l = gets.chomp.to_f

total_tintas = (h*l)/2

puts"Para pintar uma parede com #{h*l} metros quadrados, é preciso usar #{total_tintas} litros de tinta."