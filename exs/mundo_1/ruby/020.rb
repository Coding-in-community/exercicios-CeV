=begin
Desafio 020

Problema: O mesmo professor do desafio 019 quer sortear a ordem
          de apresentação de trabalhos dos alunos. Faça um programa
          que leia o nome dos quatro alunos e mostre a ordem sorteada.

Resolução do problema:
=end

alunos = []
4.times do
	print"Digite o nome do aluno: "
	a = gets.chomp
	alunos.push(a)
end

nova_ordem = alunos.shuffle

puts"A ordem de apresentação será: " 
puts *nova_ordem