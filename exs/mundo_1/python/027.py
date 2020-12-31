"""
Desafio 027

Problema: Faça um programa que leia o nome completo de uma
          pessoa, mostrando em seguida o primeiro e o último
          nome separadamente.

Resolução do problema:
"""
nome = input('Informe seu nome: ').strip().split()
print('Primeiro {} \nUltimo: {}'.format(nome[0], nome[-1]))
