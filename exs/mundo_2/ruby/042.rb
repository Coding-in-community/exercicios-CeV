=begin
Desafio 042

Problema: Refaça o desafio 035 dos triângulos, acrescentando o
          recurso de mostrar que tipo de triângulo será formado:
            - EQUILÁTERO: todos os lados iguais
            - ISÓSCELES: dois lados iguais, um diferente
            - ESCALENO: todos os lados diferentes

Resolução do problema:
=end
print"Informe a medida do lado A: "
lado_A = gets.chomp.to_f
print"Informe a medida do lado B: "
lado_B = gets.chomp.to_f
print"Informe a medida do lado C: "
lado_C = gets.chomp.to_f

if lado_A < (lado_B + lado_C) and lado_B < (lado_A + lado_C) and lado_C < (lado_A + lado_B)
    if lado_A == lado_B and lado_B == lado_C
        puts'Forma um triângulo EQUILÁTERO.'
    elsif lado_A != lado_B and lado_B != lado_C and lado_C != lado_A
        puts'Forma um triângulo ESCALENO.'
    else
        puts'Forma um triângulo ISÓSCELES.'
    end
else
    puts'Não forma um TRIÂNGULO.'
end
