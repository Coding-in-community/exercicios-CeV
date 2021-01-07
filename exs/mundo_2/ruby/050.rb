=begin
Desafio 050

Problema: Desenvolva um programa que leia seis
          números inteiros e mostre a soma apenas
          daqueles que forem pares. Se o valor for
          ímpar, desconcidere-o.

Resolução do problema:
=end

s = 0
6.times do
	print'Informe um valor: '
    n = gets.chomp.to_i
    if n % 2 == 0
        s += n
    end
end

puts"A soma de todos os valores pares informados é #{s}."
