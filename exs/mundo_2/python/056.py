"""
Desafio 056

Problema: Desenvolva um programa que leia o nome, idade e sexo
          de 4 pessoas. No final do programa,
          mostre: A média de idade do grupo.
                  Qual é o nome do homem mais velho.
                  Quantas mulheres tem menos de 20 anos.

Resolução do problemas:
"""
idadeMedia = 0
nomeHomemMaisVelho = ''
idadeHomemVelho = 0
qtdMulherMenor20 = 0

for c in range(4):
    nome = input('informe o nome da {}º pessoa: '.format(c + 1)).strip().capitalize()
    idade = int(input('Informe a idade da {}º pessoa: '.format(c + 1)))
    sexo = input('Informe o sexo da {}º pessoa: [M/F]'.format(c + 1)).strip().upper()
    print()

    idadeMedia += idade

    if sexo == 'M':
        if idade > idadeHomemVelho:
            idadeHomemVelho = idade
            nomeHomemMaisVelho = nome
    elif sexo == 'F':
        if idade < 20:
            qtdMulherMenor20 += 1

print('A idade média do grupo é de {} anos'.format(idadeMedia / 4))
print('O {} é o homem mais velho do grupo, com {} anos.'.format(nomeHomemMaisVelho, idadeHomemVelho))
print('No grupo existe {} mulher(es) com menos de 20 anos'.format(qtdMulherMenor20))
