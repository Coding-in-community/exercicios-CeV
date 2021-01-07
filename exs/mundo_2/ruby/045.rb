=begin
Desafio 045

Problema: Crie um programa que faça o computador jogar Jokenpô com você.

Resolução do problema:
=end

jogadas = ['Pedra', 'Papel', 'Tesoura']

puts'''Escolha uma jogada
[1] Pedra
[2] Papel
[3] Tesoura'''
print"Digite sua escolha: " 
opc = gets.chomp.to_i

#Tratamento de casos 
unless opc == 1..3
	puts"Digite uma opcao valida!!"
	puts'''Escolha uma jogada
[1] Pedra
[2] Papel
[3] Tesoura'''
	print"Digite sua escolha: " 
	opc = gets.chomp.to_i
end

jogada_PC = jogadas.sample

#Casos de vitoria
if opc == 1 and jogada_PC == 'Tesoura'
	puts"VOCÊ GANHOU!!!"
elsif opc == 2 and jogada_PC == 'Pedra'
	puts"VOCÊ GANHOU!!!"
elsif opc == 3 and jogada_PC == 'Papel'
	puts"VOCÊ GANHOU!!!"
	
#Casos de derrota
elsif jogada_PC == 'Tesoura' and opc == 2
	puts"VOCÊ PERDEU =("
elsif jogada_PC == 'Pedra' and opc == 3
	puts"VOCÊ PERDEU =("
elsif jogada_PC == 'Papel' and opc == 1
	puts"VOCÊ PERDEU =("

#EMPATE
else
	puts"EMPATE"
end
