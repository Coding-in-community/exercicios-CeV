"""
Desafio 061

Problema: Refaça o desafio 051, lendo o primeiro número termo e
          a razão de uma PA(Progressão Aritmética), mostrando
          os 10 primeiros termos da progressão usando a estrutura
          while.

Resolução do problema:
"""
termoPA = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

cont = 1
while cont <= 10:
    print('{} -> '.format(termoPA), end='')
    termoPA += razao
    cont += 1
print('FIM DA PROGRESSÂO.')