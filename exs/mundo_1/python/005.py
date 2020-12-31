"""
Desafio 005

Problema: Faça um programa que leia um número inteiro e mostre na tela
          o seu sucessor e antecessor.

Resolução do problema:
"""
num = int(input('Informe um valor: '))

sucessor = num + 1
antecessor = num - 1
print('Antecessor: {}\nInformado: {}\nSucessor: {}' .format(antecessor, num, sucessor))

