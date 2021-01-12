=begin
Desafio 061

Problema: Refaça o desafio 051, lendo o primeiro número termo e
          a razão de uma PA(Progressão Aritmética), mostrando
          os 10 primeiros termos da progressão usando a estrutura
          while.

Resolução do problema:
=end

print'Informe o primeiro termo da progressão: '
pa = gets.chomp.to_f

print'Informe a razão da progressão: '
r = gets.chomp.to_f 

count = 1

while count <= 10
	print pa,' '
	pa += r
	count += 1
end
