"""
Desafio 042

Problema: Refaça o desafio 035 dos triângulos, acrescentando o
          recurso de mostrar que tipo de triângulo será formado:
            - EQUILÁTERO: todos os lados iguais
            - ISÓSCELES: dois lados iguais, um diferente
            - ESCALENO: todos os lados diferentes

Resolução do problema:
"""
lado_A = float(input('Informe a medida do lado A: '))
lado_B = float(input('Informe a medida do lado B: '))
lado_C = float(input('Informe a medida do lado C: '))

if lado_A < lado_B + lado_C and lado_B < lado_A + lado_C and lado_C < lado_A + lado_B:
    print('Forma um TRIÂNGULO', end=' ')
    if lado_A == lado_B == lado_C:
        print('EQUILÁTERO.')
    elif lado_A != lado_B != lado_C != lado_A:
        print('ESCALENO.')
    else:
        print('ISÓSCELES')
else:
    print('Não forma um TRIÂNGULO.')
