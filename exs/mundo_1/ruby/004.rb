=begin
Desafio 004

Problema: Faça um programa que leia algo pelo teclado e mostre na tela
          seu tipo primitivo e todas as informações possíveis sobre ela.

Resolução do problema:
=end

print'Digite alguma coisa: '
s = gets.chomp

puts"O tipo do sue texto é (#{s.class})."
puts"Seu texto tem #{s.length} caracteres."
if s.size != 0
	puts"Seu texto não está vazio." 
else
	puts"Seu texto está vazio."
end
puts"Os 2 primeiros caracteres do seu texto são #{s[0,2]}."
puts"Seu texto em maiúsculo fica #{s.upcase}."
puts"Seu texto em minúsculo fica #{s.downcase}."
