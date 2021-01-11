=begin
Desafio 070

Problema: Crie um programa que leia o nome e o preço de vários produtos.
          O programa deverá perguntar se o usuário vai continuar.
          No final, mostre:
            A) Qual é o total gasto na compra;
            B) Quantos produtos custam mais de R$1000;
            C) Qual é o nome do produto mais barato.

Resolução do problema:
=end

qtdGasto = 0
qtdProdutos1000 = 0
precoMaisBarato = 0
nomeMaisBarato = ''
count = 1
run = true

while run
	print"Digite o nome do produto: "
	nome = gets.chomp

	print"Digite o preço do produto: "
	preco = gets.chomp.to_f

	qtdGasto += preco

	if preco > 1000
		qtdProdutos1000 += 1
	end

	if count == 1 or preco < precoMaisBarato
		nomeMaisBarato = nome
		precoMaisBarato = preco
	end

	print"Deseja comprar mais produtos? "
	opc = gets.chomp.upcase

	while opc != 'N' and opc != 'S'
		puts"Opção inválida."
		print"Deseja comprar mais produtos? "
		opc = gets.chomp.upcase
	end

	if opc == 'N'
		run = false
	end

	count += 1
end

puts"Total gasto = R$#{qtdGasto}."
puts"Você comprou #{qtdProdutos1000} produto(s) com preço maior que R$1000.00."
puts"Produto mais barato = #{nomeMaisBarato} com o preço de R$#{precoMaisBarato}."
