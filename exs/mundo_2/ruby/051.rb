=begin
Desafio 051

Problema: Desenvolva um programa que leia o primeiro termo
          e a razão PA(Progressão aritmética). No final,
          mostre os 10 primeiros termos dessa progressão.

Resolução do problema:
=end

print'Informe o primeiro termo da progressão: '
p1 = gets.chomp.to_f

print'Informe a razão da progressão: '
r = gets.chomp.to_f
n = p1 + (10 - 1) * r 

for i in (p1..n).step(r)
    puts i
end
print('FIM DA PROGRESSÂO')
