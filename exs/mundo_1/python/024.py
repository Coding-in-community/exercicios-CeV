"""
Desafio 024

Problema: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

Resolução do problema:
"""
nome = input('Cidade: ').strip().split()
print('O nome da cidade digitada começa com "SANTO": ', 'SANTO' in nome[0].upper())
