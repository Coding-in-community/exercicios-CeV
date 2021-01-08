=begin
Desafio 053

Problema: Crie um programa que leia uma frase qualquer
          e diga se ela é um palíndromo, desconsiderando
          os espaços.
          Ex: apos a sopa
              a sacada da casa
              a torre da derrota
              o lobo ama o bolo
              anotaram a data da maratona

Resolução do problemas:
=end

def is_palindromo?(s)
	q = 0
	palavra = s.delete(' ')
	for i in 1..palavra.length
		if palavra[i-1] == palavra[-i]
			q += 1
		end
	end

	if q == palavra.length
		puts"#{s} é um Palindromo."
	else
		puts"#{s} não é um Palindromo."
	end
end

print"Digite um texto ou uma palavra: "
s = gets.chomp.downcase

puts is_palindromo?(s)
