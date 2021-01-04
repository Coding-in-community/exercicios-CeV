=begin
Desafio 013

Problema: Faça um algoritmo que leia o salário de um funcionário
          e mostre seu novo salário, com 15% de aumento.

Resolução do problema:
=end

print"Digite o salário atual: "
salario = gets.chomp.to_f

aumento = (salario*1.15)
puts"O salário com 15% de aumento fica #{aumento}."
