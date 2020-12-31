"""
Desafio 051

Problema: Desenvolva um programa que leia o primeiro termo
          e a razão PA(Progressão aritmética). No final,
          mostre os 10 primeiros termos dessa progressão.

Resolução do problema:
"""
primeiroTermo = int(input('Informe o primeiro termo da progressão: '))
razao = int(input('Informe a razão da progressão: '))
n = primeiroTermo + (10 - 1) * razao # Enésimo termo da progressão

for c in range(primeiroTermo, n + 1, razao):
    print('{} -> '.format(c), end='')
print('FIM DA PROGRESSÂO')
