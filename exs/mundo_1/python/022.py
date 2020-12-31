"""
Desafio 022

Problema: Crie um programa que leia o nome completo de uma pessoa
          e mostre:
              - O nome com todas as letras maiúsculas e minúsculas.
              - Quantas letras ao todo(sem considerar espaços)
              - Quantas letras tem o primeiro nome.

Resolução do problema:
"""
nome = input('Informe seu nome completo: ').split()

print('Nome Maíusculo: ', ' '.join(nome).upper())
print('Nome minúsculo: ', ' '.join(nome).lower())
print('Quantas letras que o nome possue sem espaços: ', len(''.join(nome)))
print('Quantas letras tem o primeiro nome: ', len(nome[0]))
