=begin
Desafio 009

Problema: Faça um programa que leia um número Inteiro qualquer
          e mostre na tela a sua tabuada.

Resolução do problema:
=end

print"Qual tabuada deseja ver? "
n = gets.chomp.to_i

i = 0

while i <= 10
	puts"#{n} x #{i} = #{n*i}"
	i += 1
end