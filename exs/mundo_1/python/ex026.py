"""
Desafio 026

Problema: Faça um programa que leia uma frase pelo teclado
          e mostre quantas vezes aparece a letra "A", em que
          posição ela aparece a primeira vez e em que posição
          ela aparece a última vez.

Resolução do problema:
"""
frase = input('Digite uma frase: ').strip()

print('Quantas vezes a letra "A" apareceu: ', frase.upper().count('A'))
print('Ela aparece a primeira vez na posição: ', frase.upper().find('A') + 1)
print('Ela aparece a ultima vez na posição: ', frase.upper().rfind('A') + 1)
