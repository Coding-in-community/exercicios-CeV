=begin
Desafio 055

Problema: Faça um programa que leia o peso de cinco pessoas.
          No final, mostre qual foi o maior e o menor peso lidos.

Resolução do problema:
=end

maior = 0
menor = 0
5.times do |i|
	print"Digite o peso da #{i+1} pessoa: "
	peso = gets.chomp.to_f
	if i == 0
		menor = peso
		maior = peso
	end
	if peso > maior
		maior = peso
	end
	if peso < menor
		menor = peso
	end
end
puts "O maior peso foi #{maior}."
puts "O menor peso foi #{menor}."
