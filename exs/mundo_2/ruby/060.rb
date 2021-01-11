=begin
Desafio 060

Problema: Faça um programa que leia um número
          qualquer e mostre o seu fatorial.
          Ex: 5! = 5 x 4 X 3 X 2 X 1 = 120

Resolução do problemas:
=end

print"Qual o fatorial que deseja ver? "
n = gets.chomp.to_i

if n == 0
	puts"O fatoril de 0 é 1."
else
	a = []
	r = 1..n
	r.reverse_each do |i|
		a.push(i)
	end
	puts "O fatorial de #{n} é #{a.inject('*')}."
end
