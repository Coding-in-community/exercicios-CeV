"""
Desafio 038

Problema: Escreva um programa que leia dois números inteiros e compare-os.
          mostrando na tela uma mensagem:
            - O primeiro valor é maior
            - O segundo valor é maior
            - Não existe valor maior, os dois são iguais

Resolução do problema:
"""
numero_1 = int(input('Informe o primeiro número: '))
numero_2 = int(input('Informe o segundo número: '))

if numero_1 > numero_2:
    print('O PRIMEIRO número é MAIOR.')
elif numero_1 < numero_2:
    print('O SEGUNDO numero é MAIOR.')
else:
    print('Não existe maior, os dois são IGUAIS.')
