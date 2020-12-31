"""
Desafio 053

Problema: Crie um programa que leia uma frase qualquer
          e diga se ela é um palíndromo, desconsiderando
          os espaços.

          Ex: apos a sopa
              a sacada da casa
              a torre da derrota
              o lobo ama o bolo
              anotaram a data da maratona

Resolução do problemas:
"""
frase = input('Digite uma frase: ').strip().replace(' ', '').lower()

for idx in range(0, len(frase) // 2):  # range terá o final como a metade do comprimento da frase
    if frase[idx] == frase[-(idx + 1)]:  # frase[-(idx + 1)] percorerá a frase da última letra até a primeira
        if idx + 1 == len(frase) // 2:
            print('Essa frase informada é um palíndromo.')
            break
    else:
        print('Essa frase informada não é um palíndromo.')
        break
