=begin
Desafio 023

Problema: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Resolução do problema:
=end

print"Digite um número: "
n = gets.chomp.to_i

u = n / 1 % 10
d = n / 10 % 10
c = n / 100 % 10
m = n / 1000 % 10
puts"Unidade: #{u}\nDezena: #{d}\nCentena: #{c}\nMilhar: #{m}"