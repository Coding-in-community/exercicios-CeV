=begin
Desafio 068

Problema: Faça um programa que jogue PAR ou ÍMPAR com o computador.
          O jogo só será interrompido quando o jogador perder,
          mostrando o total de vitórias consecutivas que ele consquistou
          no fim do jogo.

Resolução do problema:
=end

def imparOuPar?(n)
	if n % 2 == 0
		true
	else
		false
	end
end

vitorias = 0
jogo = true

while jogo
	print"Par ou Ímpar? [P/I] "
	jogador = gets.chomp.upcase

	while jogador != 'P' and  jogador != 'I'
		puts"Informe um valor válido!"
		print"Par ou Ímpar? [P/I] "
		jogador = gets.chomp.upcase
	end

	randN = rand(1..10)
	pc = imparOuPar?(randN)

	if jogador == 'P' and pc == true
		puts"Ganhou!"
		puts "Computador jogou #{randN}."
		vitorias +=1
		puts"Mais uma rodada..."
	elsif jogador == 'I' and pc == false
		puts"Ganhou!"
		puts "Computador jogou #{randN}."
		vitorias +=1
		puts"Mais uma rodada..."
	else
		puts"Perdeu... =("
		puts "Computador jogou #{randN}."
		jogo = false
	end
end

puts "Máximo de vitórias consecutivas = #{vitorias}."
