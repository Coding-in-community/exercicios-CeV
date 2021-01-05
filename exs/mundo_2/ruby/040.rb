=begin
Desafio 040

Problema: Crie um programa que leia duas notas de um aluno e calcule sua média,
          mostrando uma mensagem no final, de acordo com a média atingida:
            - Média abaixo de 5.0: REPROVADO
            - Média entre 5.0 e 6.9: RECUPERAÇÃO
            - Média 7.0 ou superior: APROVADO

Resolução do problema:
=end

print"Digite sua primeira nota: "
n1 = gets.chomp.to_f

print"Digite sua segunda nota: "
n2 = gets.chomp.to_f

media = (n1 + n2)/2

if media < 5.0
	puts"REPROVADO!"
elsif 5.0 <= media and media <= 6.9
	puts"RECUPERAÇÃO!"
else
	puts"APROVADO!"
end


	
