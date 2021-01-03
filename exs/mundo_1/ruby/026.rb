=begin
Desafio 026

Problema: Faça um programa que leia uma frase pelo teclado
          e mostre quantas vezes aparece a letra "A", em que
          posição ela aparece a primeira vez e em que posição
          ela aparece a última vez.

Resolução do problema:
=end

print"Digite uma palavra: "
s = gets.chomp

puts"Na palavra #{s}, aparece #{(s.upcase).count('A')} vezes a letra A."
puts"A primeira vez que a letra A aparece na palavra #{s}, foi no índice #{(s.upcase).index('A')}."
puts"A última vez que a letra A aparece na palavra #{s}, foi no índice #{(s.upcase).rindex('A')}."