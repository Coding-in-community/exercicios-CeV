"""
Desafio 087

Problema: Aprimore o desafio anterior (86), mostrando no final:
            A) A soma de todos os valores pares digitados
            B) A soma dos valores da terceira coluna
            C) O maior valor da segunda linha

Resolução do problema:
"""
matriz = []
somaPar, somaTerceiraCol = 0, 0  # Desempacotando tupla de valores 0 para as variáveis somaPar e somaTeceiraCol

for linha in range(3):
    valor = []
    for coluna in range(3):
        valor.append(int(input(f'Informe um valor para [{linha}, {coluna}]: ')))
    matriz.append(valor)

print('-' * 32 + f'\n{"MATRIZ":^32}\n' + '-' * 32)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')

        # Somanda valores pares de toda matriz
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]
    print()

for linha in range(3):
    somaTerceiraCol += matriz[linha][2]  # Somando valores da terceira coluna

print('-' * 32)
print(f'SOMA DE VALORES PARES: {somaPar}')
print(f'SOMA DOS VALORES DA 3º COL: {somaTerceiraCol}')
print(f'MAIOR VALOR DA 2º LINHA: {max(matriz[1])}')
