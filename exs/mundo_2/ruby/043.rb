=begin
Desafio 043

Problema: Desenvolva uma lógica que leia o peso e a altura de
          uma pessoa, calcule seu Índice de Massa Corporal (IMC)
          e mostre seu status, de acordo com a tabela abaixo:
            - IMC abaixo de 18,5: Abaixo do Peso
            - Entre 18,5 e 25: Peso Ideal
            - 25 até 30: Sobrepeso
            - 30 até 40: Obesidade
            - Acima de 40: Obesidade Mórbida

Resolução do problema:
=end

print"Digite seu peso: "
peso = gets.chomp.to_f
print"Digite sua altura: "
altura = gets.chomp.to_f

imc = peso/(altura**2)

puts"Seu imc é %.2f." % imc
if 0 < imc and imc < 18.5
	puts"Abaixo do peso."
elsif 18.5 <= imc and imc < 25
	puts"Peso ideal."
elsif 25 <= imc and imc < 30
	puts"Sobrepeso."
elsif 30 <= imc and imc < 40
	puts"Obesidade."
else
	puts"Obesidade mórbida."
end
