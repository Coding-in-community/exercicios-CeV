=begin
Desafio 007

Problema: Desenvolva um programa que leia as duas notas de um aluno,
          calcule e mostre a sua média.

Resolução do problema:
=end

print"Digite a primeira nota: "
n1 = gets.chomp.to_f
print"Digite a segunda nota: "
n2 = gets.chomp.to_f

media = (n1+n2)/2

puts"a média é igual a #{media}."