"""
Desafio 060

Problema: Faça um programa que leia um número
          qualquer e mostre o seu fatorial.

          Ex: 5! = 5 x 4 X 3 X 2 X 1 = 120

Resolução do problemas:
"""
num = int(input('Informe um valor para calcular: '))

fatorial = 1
cont = num
print('{}! -> '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')

    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial))
