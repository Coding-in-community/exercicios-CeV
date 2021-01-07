=begin
Desafio 052

Problema: Faça um programa que leia um número
          inteiro e diga se ele é ou não um número
          primo.

Resolução do problemas:
=end

def is_prime(n)
	q = 0
	for i in 1..n
		if n % i == 0
			q += 1
		end
	end
	if q == 2
		return true
	else
		return false
	end
end

print"Digite um número: "
n = gets.chomp.to_i

puts"O número #{n} é primo? #{is_prime(n)}"
