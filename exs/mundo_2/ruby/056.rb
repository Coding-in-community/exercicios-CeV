=begin
Desafio 056

Problema: Desenvolva um programa que leia o nome, idade e sexo
          de 4 pessoas. No final do programa,
          mostre: A média de idade do grupo.
                  Qual é o nome do homem mais velho.
                  Quantas mulheres tem menos de 20 anos.

Resolução do problemas:
=end

media = 0
nomeHomemVelho = ''
idadeHomemVelho = 0
qtdMulheresMenores = 0


4.times do |i|
	print"Digite o nome da #{i+1} pessoa: "
	nome = gets.chomp.capitalize
	print"Digite a idade da #{i+1} pessoa: "
	idade = gets.chomp.to_i
	print"Digite o sexo da #{i+1} pessoa [M/F]: "
	sexo = gets.chomp.capitalize

	if idade > idadeHomemVelho and sexo == 'M'
		idadeHomemVelho = idade 
		nomeHomemVelho = nome
	elsif idade <= 20 and sexo == 'F'
		qtdMulheresMenores += 1
	end
end

puts "O homem mais velho é o #{nomeHomemVelho} que tem #{idadeHomemVelho} anos."
puts "Tem #{qtdMulheresMenores} mulher(es) menor(es) que 20 anos."
