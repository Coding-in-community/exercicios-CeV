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
	print"Digite o ano de nascimento da #{i+1} pessoa: "
	anoNasc = gets.chomp.to_i
	idade = Time.now.year - anoNasc
	if idade >= 21
		maiores += 1
	else
		menores += 1
	end
end
puts "Tem #{maiores} pessoas maiores de idade."
puts "Tem #{menores} pessoas menores de idade."
