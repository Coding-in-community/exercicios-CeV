=begin
Desafio 041

Problema: A Confederação Nacional de Natação precisa de um programa
          que leia o ano de nascimento de um atleta e mostre sua
          categoria, de acordo com a idade:
            - Até 9 anos: MIRIM
            - Até 14 anos: INFANTIL
            - Até 19 anos: JÚNIOR
            - Até 25 anos: SÊNIOR
            - Acima de 25 anos: MASTER

Resolução do problema:
=end

print"Qual o ano do seu nascimento? "
anoNasc = gets.chomp.to_i

anoAtual = Time.now.year
idade = anoAtual - anoNasc


case idade
when 0..9
	puts"Atleta MIRIM"
when 10..14
	puts"Atleta INFANTIL"
when 15..19
	puts"Atleta JÚNIOR"
when 20..25
	puts"Atleta SÊNIOR"
else
	puts"Atleta MASTER"
end
