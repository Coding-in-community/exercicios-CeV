=begin
Desafio 032

Problema: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

Resolução do problema:
=end

print"Digite um ano qualquer: "
ano = gets.chomp.to_i

if ano == 0
	ano = Time.now.year
end

if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0)
	puts"O ano #{ano} é bissexto."
else
	puts"O ano #{ano} não é bissexto."
end