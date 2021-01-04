=begin
Desafio 004

Problema: Faça um programa que leia algo pelo teclado e mostre na tela
          seu tipo primitivo e todas as informações possíveis sobre ela.

Resolução do problema:
=end
class String
	def is_alnum?()
		!!match(/^[[:alnum:]]+$/)
	end

	def is_alpha?()
		!!match(/^[[:alpha:]]$/)
	end

	def is_letter?()
	    !!match?(/[[:alpha:]]/)
	end

	def is_space?()
		!!match?(/[[:space:]]/)
	end

	def is_lower?()
		!!match?(/[[:lower:]]/)
	end

	def is_upper?()
		!!match?(/[[:upper:]]/)
	end

	def is_capitalized?()
		chars.first == chars.first.upcase
	end

	def is_printable?()
		!!match?(/\p{Print}/)
	end

	def is_digit?()
		!!match?(/\p{Digit}/)
	end

	def is_decimal?()
		!!match?(/\p{Nd}/)
	end

	def is_num?()
		!!match?(/\p{N}/)
	end
end


def is_indentifier?(s)
	words = ['BEGIN', 'END','begin','alias', 'and','break','case', 'class',
		'def','module','next','nil','not','or','redo','rescue','retry','return',
		'elsif','end','false','ensure','for','if','true','undef','unless','do',
		'else','super','then','until','when','while','defined?','self']
	
	words.each do |i|
		if i == s
			return true
		else
			return false
		end
	end
end


print('Digite algo: ')
s = gets.chomp

puts"O tipo primitivo desse valor é: #{s.class}"
puts"É um número? #{s.is_num?}"
puts"É um valor alfanumérico? #{s.is_alnum?}"
puts"É texto? #{s.is_alpha?}"
puts"É um digito? #{s.is_digit?}"
puts"É um identificador? #{is_indentifier?(s)}"
puts"Está em letra minúscula? #{s.is_lower?}"
puts"Está em letra maiúscula? #{s.is_upper?}"
puts"É uma tabela de impressão? #{s.is_printable?}"
puts"É um espaço? #{s.is_space?}"
puts"Está capitalizada? #{s.is_capitalized?}"

