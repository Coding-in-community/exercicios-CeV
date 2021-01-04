=begin
Desafio 005

Problema: Faça um programa que leia um número inteiro e mostre na tela
          o seu sucessor e antecessor.

Resolução do problema:
=end

print"Digite um número: "
n = gets.chomp.to_i
puts"o antecessor de #{n} é #{n-1}, e seu sucessor é #{n+1}."