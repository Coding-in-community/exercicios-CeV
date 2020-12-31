"""
Desafio 082

Problema: Crie um programa que vai ler vários números e colocar em uma lista.
          Depois disso, crie duas listas extras que vão conter apenas os valores
          pares e valores ímpares digitados, respectivamente.
          Ao final, mostre o conteúdo das três listas geradas.

Resolução do problema:
"""
listaNumeros, lista_par, lista_impar = [], [], []
contador = 0
while True:
    listaNumeros.append(int(input(f'Digite o {contador + 1}º número: ')))
    print('-' * 35)
    contador += 1

    continuar = input('Novo número? [S/N]: ').strip().upper()

    while continuar not in ('S', 'N'):
        print('\nInforme a opção correta...')
        continuar = input('Novo número? [S/N]: ').strip().upper()
    print('-' * 35)

    if continuar == 'N':
        print('-' * 35 + f'\n{"VALORES CADASTRADOS COM SUCESSO":^35}\n' + '-' * 35)
        print(f'Lista de todos valores: {listaNumeros}')
        break

for valor in listaNumeros:
    lista_par.append(valor) if valor % 2 == 0 else lista_impar.append(valor)

print(f'Lista valores PARES: {lista_par}')
print(f'Lista valores ÍMPARES: {lista_impar}')
