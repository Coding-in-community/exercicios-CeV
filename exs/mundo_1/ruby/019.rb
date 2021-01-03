=begin
Desafio 019

Problema: Um professor quer sortear um dos seus quatro alunos para
          apagar o quadro. Faça um programa que ajude ele, lendo o
          nome dos alunos e escrevendo na tela o nome do escolhido.

Resolução do problema:
=end

alunos = []
4.times do
	print"Digite o nome do aluno: "
	a = gets.chomp
	alunos.push(a)
end

aluno_aleatorio = alunos.sample
puts"O aluno que irá apagar a lousa é o(a) #{aluno_aleatorio}."