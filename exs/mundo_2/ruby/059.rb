=begin
Desafio 059

Problema: Crie um programa que leia dois valores
          e mostre um menu na tela.
          -------- Menu --------
          [1] - Somar
          [2] - Multiplicar
          [3] - Maior
          [4] - Novos números
          [5] - Sair do programa
          -----------------------
          Seu programa deverá realizar a operação solicidade em cada caso.

Resolução do problemas:
=end

menu = '''
-------- Menu --------
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair do programa
-----------------------'''

def somar(n1, n2)
	"Resultado adição = #{n1 + n2}."
end

def multiplicar(n1, n2)
	"Resultado multiplição = #{n1 * n2}."
end

def maior(n1, n2)
	if n1 > n2
		"O maior número é o #{n1}."
	elsif n1 < n2
		"O maior número é o #{n2}."
	else
		"Os dois números são iguais."
	end
end

def get_numbers()
	print"Digite o primeiro número: "
	n1 = gets.chomp.to_i
	print"Digite o segundo número: "
	n2 = gets.chomp.to_i
	return n1, n2
end

opc = 0
n1, n2 = get_numbers
while opc != 5
	puts menu

	print"Digite uma operação: "
	opc = gets.chomp.to_i

	if opc > 5 or opc <= 0
		puts"Digite um operação válida."
	end

	if opc == 1
		puts somar(n1, n2)

	elsif opc == 2
		puts multiplicar(n1, n2)

	elsif opc == 3
		puts maior(n1, n2)

	elsif opc == 4
		n1, n2 = get_numbers

	elsif opc == 5
		puts 'finalizando...'
	end
end
puts "Processo encerrado em #{Time.now}."
