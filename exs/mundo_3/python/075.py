"""
Desafio 075

Problema: Desenvolva um programa que leia quatro valores pelo teclado
          e guarde-os em uma tupla.

          No final, mostre:
            A) Quantas vezes apareceu o valor 9;
            B) Em que posição foi digitado o primeiro valor 3;
            C) Quais foram os números pares.

Resolução do problema:
"""
# Inserindo valores na tupla
valores = tuple(int(input(f'Digite o {cont + 1}º valor: ')) for cont in range(4))

print(f'\nO valor 9 apareceu: {valores.count(9)} vezes')

if valores.count(3) != 0:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados: ', end='')
for numero in valores:
    if numero % 2 == 0:
        print(numero, end=' ')
