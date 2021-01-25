=begin
Desafio 031

Problema: Desenvolva um programa que pergunte a distância de
          uma viagem em Km. Calcule o preço da passagem, cobrando
          R$0,50 por Km para viagens de até 200Km e R$0,45 para
          viagens mais longas.

Resolução do problema:
=end

print'Informe a distância em KM: '
d = gets.chomp.to_f

if d > 200
	preco = d * 0.45
else
	preco = d * 0.50
end

puts"O valor da passagem será R$ #{preco}."