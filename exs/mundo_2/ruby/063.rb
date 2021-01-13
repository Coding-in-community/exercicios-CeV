=begin
Desafio 063

Problema: Escreva um programa que leia um número N inteiro qualquer
          e mostre na tela os N primeiros elementos de uma sequência de Fibonacci.
          Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

Resolução do problema:
=end

c = 0 
fib = 0
s = 1

print"Quantos números da sequência Fibonacci deseja ver? "
n = gets.chomp.to_i

while c < n
	print fib, " "
	fib = s
	s = fib + s
	c += 1
end
