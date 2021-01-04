=begin
Desafio 034

Problema: Escreva um programa que pergunte o salário de um funcionário
          e calcule o valor do seu aumento. Para salários superiores a
          R$1250,00, calcule um aumento de 10%. Para os inferiores ou
          iguais, o aumento é de 15%.

Resolução do problema:
=end

print'Informe seu salário: R$'
salario = gets.chomp.to_i

if salario <= 1250.00
    aumento = (salario * 1.15)
else
    aumento = (salario * 1.10)
end

puts"O salário com aumento é: R$#{aumento}"