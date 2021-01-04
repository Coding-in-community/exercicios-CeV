=begin
Desafio 035

Problema: Desenvolva um programa que leia o comprimento de três
          retas e diga ao usuário se elas podem ou não formar um triângulo.

Resolução do problema:
=end

print'Informe a medida do lado A: '
a = gets.chomp.to_f

print'Informe a medida do lado B: '
b = gets.chomp.to_f

print'Informe a medida do lado C: '
c = gets.chomp.to_f

analise = false

if (b-c).abs < 1 and 1 < b + c 
	if (a -c ).abs < b and b < a + c
		if (a - b).abs < c and c < a + b
			analise = true
		end
	end
end
if analise
    puts'As retas PODEM FORMAR um triângulo.'
else
    puts'As retas NÃO PODEM FORMAR um triângulo.'
end