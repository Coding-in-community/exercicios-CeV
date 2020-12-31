"""
Desafio 019

Problema: Um professor quer sortear um dos seus quatro alunos para
          apagar o quadro. Faça um programa que ajude ele, lendo o
          nome dos alunos e escrevendo na tela o nome do escolhido.

Resolução do problema:
"""
from random import choice
nome1 = input('1º aluno(a): ')
nome2 = input('2º aluno(a): ')
nome3 = input('3º aluno(a): ')
nome4 = input('4º aluno(a): ')

escolhido = choice([nome1, nome2, nome3, nome4])

print('O aluno escolhido foi: ', escolhido)
