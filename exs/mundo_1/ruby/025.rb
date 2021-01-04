=begin
Desafio 025

Problema: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

Resolução do problema:
=end

print"Digite seu nome: "
n = gets.chomp.upcase

if n.index('SILVA') != nil
	puts"Você tem Silva no nome." 
else
	puts"Você não tem Silva no nome."
end