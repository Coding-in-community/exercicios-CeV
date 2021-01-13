=begin
Desafio 071

Problema: Crie um programa que simule o funcionamento de um caixa eletrônico.
          No início, pergunte ao usuário qual será o valor a ser sacado(Número inteiro)
          e o programa vai informar quantas cédulas de cada valor serão entregues.
          OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

Resolução do problema:
=end

puts"CAIXA ELETRÔNICO"
print"Quanto deseja sacar? "
saque = gets.chomp.to_f

valorSaque = saque

cedula50 = 0
cedula20 = 0
cedula10 = 0
cedula1  = 0


while valorSaque != 0
	if valorSaque >= 50
		valorSaque -= 50
		cedula50 += 1
	elsif valorSaque >= 20
		valorSaque -= 20
		cedula20 += 1
	elsif valorSaque >= 10
		valorSaque -= 10
		cedula10 += 1
	elsif valorSaque >= 1
		valorSaque -= 1
		cedula1 += 1
	end
end
	
puts"Foram sacadas #{cedula50} cédulas de 50."
puts"Foram sacadas #{cedula20} cédulas de 20."
puts"Foram sacadas #{cedula10} cédulas de 10."
puts"Foram sacadas #{cedula1} cédulas de 1."
