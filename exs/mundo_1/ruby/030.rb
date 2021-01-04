=begin
Desafio 030

Problema:  Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

Resolução do problema:
=end

print'Digite um número: '
n = gets.chomp.to_i

if n % 2 == 0
	puts"O número #{n} é par."
else
	puts"O número #{n} é ímpar."
end