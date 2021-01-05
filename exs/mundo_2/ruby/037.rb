=begin
Desafio 037

Problema: Escreva um programa em Python que leia um número
          inteiro qualquer e peça para o usuário escolher qual
          será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

Resolução do problema:
=end

def to_bin(n)
	n.to_s(2)
	#pode fazer assim também
	#"%b" % n
end

def to_hex(n)
	n.to_s(16)
	#pode fazer assim também
	#"%x" % n
end

def to_oct(n)
	n.to_s(8)
	#pode fazer assim também
	"%o" % n
end

print"Digite um número: "
n = gets.chomp.to_i 

puts"Deseja ver o número #{n} em qual formato?"
print"[1]binário [2]hexadecimal [3]octal  "
opc = gets.chomp.to_i

if opc == 1
	puts"O número #{n} em binário fica:\n#{to_bin(n)}"
elsif opc == 2
	puts"O número #{n} em hexadecimal fica:\n#{to_hex(n)}"
elsif opc == 3
	puts"O número #{n} em octal fica:\n#{to_oct(n)}"
else 
	abort('Opção inválida. Abortando...')	
end
