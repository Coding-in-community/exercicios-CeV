"""
Desafio 020

Problema: O mesmo professor do desafio 019 quer sortear a ordem
          de apresentação de trabalhos dos alunos. Faça um programa
          que leia o nome dos quatro alunos e mostre a ordem sorteada.

Resolução do problema:
"""
from random import shuffle
nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')

ordem = [nome1, nome2, nome3, nome4]
shuffle(ordem)
print('Ordem: {}'.format(ordem))
