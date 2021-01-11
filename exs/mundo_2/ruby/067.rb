=begin
Desafio 067

Problema: Faça um programa que mostre a tabuada de vários números,
          um de cada vez, para cada valor digitado pelo usuário.
          O programa será interrompido quando o número solicitado
          for negativo.

Resolução do problema:
=end

run = true

while run
	print"Qual tabuada deseja ver? "
	n = gets.chomp.to_i

	if n < 0
		run = false
	else
		11.times do |i|
			puts "#{i} x #{n} = #{i*n}"
		end
	end
end
puts"Até outra hora!"
