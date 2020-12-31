"""
Desafio 086

Problema: Crie um programa que crie uma matriz 3x3 e preencha com valores lidos
          pelo teclado.
          No final, mostre a matriz na tela, com a formatação correta.

Resolução do problema:
"""
matriz = []

for linha in range(3):
    valor = []
    for coluna in range(3):
        valor.append(int(input(f'Informe o valor para [{linha}, {coluna}]: ')))
    matriz.append(valor)

print()
print('-' * 21 + f'\n{"MATRIZ":^22}\n' + '-' * 21)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
