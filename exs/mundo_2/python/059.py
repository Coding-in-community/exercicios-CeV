"""
Desafio 059

Problema: Crie um programa que leia dois valores
          e mostre um menu na tela.

          -------- Menu --------
          [1] - Somar
          [2] - Multiplicar
          [3] - Maior
          [4] - Novos números
          [5] - Sair do programa
          -----------------------

          Seu programa deverá realizar a operação solicidade em cada caso.

Resolução do problemas:
"""
menu = '''
-------- Menu --------
[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair do programa
-----------------------'''

priValor = int(input('Informe o primeiro valor: '))
segValor = int(input('Informe o segundo valor: '))

op = 0
while op != 5:
    print(menu)
    op = int(input('Qual das opção deseja realizar: '))

    if op == 1:
        print('\nA soma de {} + {} é igual a {}'.format(priValor, segValor, priValor + segValor))
    elif op == 2:
        print('\nA multiplicação de {} X {} é igual a {}'.format(priValor, segValor, priValor * segValor))
    elif op == 3:
        print('\nO maior valor informado é {}'.format(max(priValor, segValor)))
    elif op == 4:
        priValor = int(input('\nInforme um novo primeiro valor: '))
        segValor = int(input('Informe um novo segundo valor: '))
    elif op == 5:
        print('Finalizando. . .')
print('\nPROGRAMA FINALIZADO.')
