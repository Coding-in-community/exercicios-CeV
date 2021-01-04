=begin
Desafio 022

Problema: Crie um programa que leia o nome completo de uma pessoa
          e mostre:
              - O nome com todas as letras maiúsculas e minúsculas.
              - Quantas letras ao todo(sem considerar espaços)
              - Quantas letras tem o primeiro nome.

Resolução do problema:
=end

print'Digite seu nome completo: '
nome = gets.chomp

puts"Nome maiúsculo: #{nome.upcase}"
puts"Nome minúsculo: #{nome.downcase}"
puts"Total de letras do nome sem espaços: #{nome.delete(' ').length}"
puts"Total de letras do primeiro nome: #{(nome.split)[0].length}"