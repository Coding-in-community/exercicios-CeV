=begin
Desafio 048

Problema: Faça um programa que calcule a soma entre todos os
          números ímpares que são múltiplos de três e que se
          encontram no intervalo de 1 até 500.

Resolução do problema:
=end

s = 0

for i in (0..500)
	if i % 2 != 0
		if i % 3 == 0
			s += i
		end	
	end
end


puts"A soma de todos os números ímpares múltiplos de 3 é #{s}."