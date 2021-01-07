=begin
Desafio 054

Problema: Crie um programa que leia o ano de nascimento
          de sete pessoas. No final, mostre quantas pessoas
          ainda não atingiram a maioridade e quantas já são maiores.

Resolução do problemas:
=end

maiores = 0
menores = 0
7.times do |i|
	print"Digite a idade da #{i+1} pessoa: "
	idade = gets.chomp.to_i
	if idade >= 18
		maiores += 1
	end
	menores += 1
end

puts "Tem #{maiores} pessoas maiores de idade."
puts "Tem #{menores} pessoas menores de idade."
