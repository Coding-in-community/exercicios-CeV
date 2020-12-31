"""
Desafio 035

Problema: Desenvolva um programa que leia o comprimento de três
          retas e diga ao usuário se elas podem ou não formar um triângulo.

Resolução do problema:
"""
lado_A = float(input('Informe a medida do lado A: '))
lado_B = float(input('Informe a medida do lado B: '))
lado_C = float(input('Informe a medida do lado C: '))
analise = False
#  Somente será validado como Triângulo passando nas três condições seguintes
if abs(lado_B - lado_C) < lado_A < lado_B + lado_C:
    if abs(lado_A - lado_C) < lado_B < lado_A + lado_C:
        if abs(lado_A - lado_B) < lado_C < lado_A + lado_B:
            analise = True
if analise:
    print('As retas PODEM FORMAR um triângulo.')
else:
    print('As retas NÃO PODEM FORMAR um triângulo.')
