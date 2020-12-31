"""
Desafio 062

Problema: Melhore o desafio 061, perguntando para o usuário se ele
          quer mostrar mais alguns termos. O programa encerra quando
          ele disser que quer mostrar 0 termos.

Resolução do problema:
"""
termoPA = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

cont = -1
cont2 = 1
enesimoTermo = 10

while cont != 0:
    while cont2 <= enesimoTermo:
        print('{} -> '.format(termoPA), end='')
        termoPA += razao

        cont2 += 1
    print('AGUARDANDO')
    op = int(input('\nVer mais quantos valores: '))

    if op != 0 and 0 < op:
        enesimoTermo += op
    else:
        cont = 0

print('FIM DA PROGRESSÃO.')