=begin
Desafio 024

Problema: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

Resolução do problema:
=end

print"Digite o nome de uma cidade: "
n = gets.chomp

if (n.upcase).start_with?('SANTO')
	puts"A cidade informada começa com Santo."
else
	puts"A cidade informada não começa com Santo."
end