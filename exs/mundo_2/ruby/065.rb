=begin
Desafio 065

Problema: Crie um programa que leia vários números inteiros pelo teclado.
          No final da execução, mostre a média entre todos os valores e
          qual foi o maior e menor valor lido. O programa deve perguntar
          ao usuário se ele quer ou não continuar a digitar valores.

Resolução do problema:
=end

maior = 0
menor = 0
numeros = []
run = true

while run
	print"Digite um número: "
	n = gets.chomp.to_i

	print"Deseja informar mais valores? "
	opc = gets.chomp.upcase
	if opc == 'N'
		run = false
	end

	if maior == 0 and menor == 0
		maior = n 
		menor = n
	else
		if n > maior
			maior = n 
		elsif n < menor
			menor = n
		end
	end
	numeros.push(n)
end

media = (numeros.inject("+").to_f)/numeros.length
puts "A média dos números é #{media}."
puts "O maior número digitado foi #{maior}."
puts "O menor número digitado foi #{menor}."
