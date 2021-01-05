=begin
Desafio 039

Problema: Faça um programa que leia o ano de nascimento de um jovem e informe,
          de acordo com a sua idade, se ele ainda vai se alistar ao serviço
          militar, se é a hora exata de se alistar ou se já passou do tempo
          do alistamento. Seu programa também deverá mostrar o tempo que falta
          ou que passou do prazo.

Resolução do problema:
=end

anoAtual = Time.now.year
print"Digite o ano do seu nascimento: "
ano = gets.chomp.to_i
idade = anoAtual - ano

if idade < 18
	puts"Ainda irá se alistar."
	puts"Você deverá se alistar daqui #{18 - idade} ano(s), em #{anoAtual + (18 - idade)}."
elsif idade == 18
	puts"Você deverá se alistar neste ano!"
else
	puts"Já passou da hora de se alistar!"
	puts"Você deveria ter se alistado há #{idade - 18} ano(s), em #{anoAtual - (idade - 18)}."
end

