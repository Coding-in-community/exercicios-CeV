=begin
Desafio 029

Problema: Escreva um programa que leia a velocidade de um carro.
          Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
          que ele foi multado. A multa vai custar R$7,00 por cada
          Km acima do limite.

Resolução do problema:
=end

print'Informe a velocidade do carro: '
v = gets.chomp.to_i

if v > 80:
    puts'Você foi multado.'
    multa = (v - 80) * 7.00
    puts"Você vai pagar R$#{multa} de multa."
else
	puts'Ta na velocidade certa!'
end