=begin
Desafio 064

Problema: Crie um programa que leia vários números inteiros pelo teclado.
          O programa só vai parar quando o usuário digitar o valor 999,
          que é a condição de parada. No final, mostre quantos números
          foram digitados e qual foi a soma entre eles.
          Desconsiderando o flag(999).

Resolução do problema:
=end

count = 0
soma = []
n = 0
while n != 999
	print"Digite um número: "
	n = gets.chomp.to_i
	if n != 999
		soma.push(n)
		count += 1
	else
		puts"A soma dos valores #{count} digitados é igual a #{soma.inject("+")}."
	end
end
