=begin
Desafio 062

Problema: Melhore o desafio 061, perguntando para o usuário se ele
          quer mostrar mais alguns termos. O programa encerra quando
          ele disser que quer mostrar 0 termos.

Resolução do problema:
=end

print'Informe o primeiro termo da progressão: '
pa = gets.chomp.to_f

print'Informe a razão da progressão: '
r = gets.chomp.to_f 

count = 1
e = 10
run = true

while run
	while count <= e
		print pa,' '
		pa += r
		count += 1
	end
	puts"\nDeseja ver mais quantos valores? "
	op = gets.chomp.to_i

	if op != 0
		e += op
	else
		run = false
		print"Encerrando..."
	end
end
