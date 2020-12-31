"""
Desafio 066

Problema: Crie um programa que leia varios números inteiros pelo teclado.
          O programa só vai parar quando o usuário digitar o valor 999,
          que é a condição de parada. No final, mostre quantos números
          foram digitados e qual foi a soma entre eles (desconsiderando
          o flag).

Resolução do problema:
"""
somador = contador = 0
while True:
    numero = int(input(f'Informe o {contador + 1}º número ou 999 para sair: '))

    if numero == 999:
        break

    somador += numero
    contador += 1

print(f'\nForam informados {contador} números\nA soma entre todos os números é: {somador}')
