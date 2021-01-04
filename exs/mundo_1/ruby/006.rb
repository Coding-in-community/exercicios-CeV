=begin
Desafio 006

Problema: Crie um algoritmo que leia um número e mostre o seu drobro,
          triplo e raiz quadrada.

Resolução do problema:
=end
print"Digite um número: "
n = gets.chomp.to_i
dobro = n*2
triplo = n*3
raiz = n**0.5
puts"o dobro de #{n} é #{dobro}."
puts"o triplo de #{n} é #{triplo}."
puts"a raiz quadrada de #{n} é #{raiz}."