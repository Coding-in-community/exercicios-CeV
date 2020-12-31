"""
Desafio 067

Problema: Faça um programa que mostre a tabuada de vários números,
          um de cada vez, para cada valor digitado pelo usuário.
          O programa será interrompido quando o número solicitado
          for negativo.

Resolução do problema:
"""
print('-' * 20)
print(f'{" Tabuada v3.0 ":~^20}')
print('-' * 20)

while True:
    tabuada = int(input('Tabuada desejada: '))
    print('-' * 20)

    if tabuada < 0:
        break

    for cont in range(0, 11):
        print(f'{tabuada} x {cont:2} = {tabuada * cont:2}')
    print('-' * 20)

print(f'{" TABUADA FINALIZADA ":~^30}\nFOI UM PRAZER AJUDA-LO!!!')
