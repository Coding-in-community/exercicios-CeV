=begin
Desafio 058

Problema: Melhore o jogo do desafio 028 onde o computador vai "pensar" em um
          número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
          acertar, mostrando no final quantos palpites foram necessários para vencer.

Resolução do problemas:
=end

pc = rand(1..10)
chutes = 0
acertou = false

until acertou
	print"Qual o seu palpite? "
	n = gets.chomp.to_i
	if n == pc
		chutes += 1
		acertou = true
	elsif n < pc
		puts"mais que isso!"
		chutes += 1
	elsif n > pc
		puts"menos que isso!"
		chutes += 1
	end
end

puts"Acertou com #{chutes} tentativas!"
