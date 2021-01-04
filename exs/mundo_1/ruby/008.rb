=begin
Desafio 008

Problema: Escreva um programa que leia um valor em metros e o
          exiba convertido em centímetros e milímetros.

Resolução do problema:
=end

print"Digite a medida em metros: "
medida = gets.chomp.to_f

cm = medida*100
mm = medida*1000

puts"#{medida} em centimetros é igual a #{cm}."
puts"#{medida} em milimetros é igual a #{mm}."
