=begin
Desafio 014

Problema: Escreva um programa que converta uma temperatura
          digitando em graus Celsius e converta para graus Fahrenheit.

Resolução do problema:
=end

print"Qual a temperatura em Celcius? "
celcius = gets.chomp.to_f

fahrenheit = 1.8 * celcius + 32

puts"#{celcius} Celcius em Fahrenheit é #{fahrenheit}."