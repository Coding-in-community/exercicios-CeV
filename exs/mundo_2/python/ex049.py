"""
Desafio 049

Problema: Refaça o desafio 009, mostrando tabuada de um
          número que o usuário escolher, só que agora
          utilizando um laço FOR.

Resolução do problema:
"""
tabuada = int(input('Informe a tabuada que deseja ver: '))

for c in range(0, 11):
    print('{} X {:2} = {}'.format(tabuada, c, tabuada * c))
