"""
Desafio 040

Problema: Crie um programa que leia duas notas de um aluno e calcule sua média,
          mostrando uma mensagem no final, de acordo com a média atingida:
            - Média abaixo de 5.0: REPROVADO
            - Média entre 5.0 e 6.9: RECUPERAÇÃO
            - Média 7.0 ou superior: APROVADO

Resolução do problema:
"""
nota_1 = float(input('Informe a primeira nota: '))
nota_2 = float(input('Informe a segunda nota: '))

media = (nota_1 + nota_2) / 2

if media < 5.0:
    print('REPROVADO.')
elif 5.0 <= media <= 6.9:
    print('RECUPERAÇÃO.')
else:
    print('APROVADO')
