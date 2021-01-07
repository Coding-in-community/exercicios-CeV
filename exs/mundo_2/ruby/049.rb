=begin
Desafio 049

Problema: Refaça o desafio 009, mostrando tabuada de um
          número que o usuário escolher, só que agora
          utilizando um laço FOR.

Resolução do problema:
=end

print"Qual tabuada deseja ver? "
n = gets.chomp.to_i

for i in 1..10
	puts"#{n} x #{i} = #{n*i}"
end
