=begin
Desafio 033

Problema: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

Resolução do problema:
=end

print'Digite o primeiro número: '
num1 = gets.chomp.to_f

print'Digite o segundo número: '
num2 = gets.chomp.to_f

print'Digite o terceiro número: '
num3 = gets.chomp.to_f

maior = num1
menor = num1

if num2 > num1 and num2 > num3
    maior = num2
end

if num3 > num1 and num3 > num2
    maior = num3
end

if num2 < num1 and num2 < num3
    menor = num2
end

if num3 < num1 and num3 < num2
    menor = num3
end

puts"O número #{maior} é o MAIOR!"
puts"O número #{menor} é o MENOR!"