=begin
Desafio 057

Problema: Faça um programa que leia o sexo de uma pessoa. Mas só aceite
          os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
          até ter um valor correto.

Resolução do problemas:
=end

sexo = ''

while sexo != 'M' and sexo != 'F'
	print"Digite seu sexo [M/F]: "
	sexo = gets.chomp.upcase

	if sexo != 'M' and sexo !='F'
		puts"Sexo invalido."
	end
end

puts "Sexo #{sexo} cadastrado com sucesso."
