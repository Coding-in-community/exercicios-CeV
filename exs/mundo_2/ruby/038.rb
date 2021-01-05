=begin
Desafio 038

Problema: Escreva um programa que leia dois números inteiros e compare-os.
          mostrando na tela uma mensagem:
            - O primeiro valor é maior
            - O segundo valor é maior
            - Não existe valor maior, os dois são iguais

Resolução do problema:
=end

print"Digite o primeiro número: "
n1 = gets.chomp.to_i

print"Digite o segundo número: "
n2 = gets.chomp.to_i

if n1 > n2
	puts"#{n1} é maior que #{n2}."
elsif n1 < n2
	puts"#{n2} é maior que #{n1}."
else
	puts"Os dois números são iguais."
end
