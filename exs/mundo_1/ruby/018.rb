=begin
Desafio 018

Problema: Faça um programa que leia um ângulo qualquer e mostre na
          tela o valor do seno, cosseno e tangente desse ângulo.

Resolução do problema:
=end

print"Digite o valor do ângulo: "
a = gets.chomp.to_f

seno = Math.sin(a)
cosseno = Math.cos(a)
tangente = Math.cos(a)

puts"O seno do ângulo #{a} é #{seno}."
puts"O cosseno do ângulo #{a} é #{cosseno}."
puts"A tangente do ângulo #{a} é #{tangente}."