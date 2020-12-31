"""
Desafio 081

Problema: Crie um programa que vai ler vários números e colocar em uma lista.
          Depois disso, mostre:
            A) Quantos números foram digitados;
            B) A lista de valores ordenada de forma decrescente.
            C) Se o valor 5 foi digitado e está ou não na lista.

Resolução do problema:
"""
listaNumeros = []

contNumero = 0
while True:
    listaNumeros.append(int(input(f'Informe o {contNumero + 1}º número: ')))
    contNumero += 1
    print('-' * 35)

    continuar = input('Outro número? [S/N]: ').strip().upper()

    while continuar not in ('S', 'N'):
        print('\nInforme a opção corretamente...')
        continuar = input('Outro número? [S/N]: ').strip().upper()
    print('-' * 35)

    if continuar == 'N':
        print(f'\nVocê digitou {contNumero} valores')
        listaNumeros.sort(reverse=True)
        print(f'Lista de valores em ordem decrescente: {listaNumeros}')

        if 5 in listaNumeros:
            for idx, valor in enumerate(listaNumeros):
                if valor == 5:
                    print(f'O valor 5 foi encontrado na lista na posição {idx}')
                    break
        else:
            print('O valor 5 não foi encontrado na lista')
        break

