=begin
Desafio 027

Problema: Faça um programa que leia o nome completo de uma
          pessoa, mostrando em seguida o primeiro e o último
          nome separadamente.

Resolução do problema:
=end
print('Digite seu nome: ')
nome = gets.chomp.strip.split
puts"Primeiro nome: #{nome[0]}."
puts"Último nome: #{nome[-1]}."