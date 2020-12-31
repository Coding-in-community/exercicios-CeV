"""
Desafio 065

Problema: Crie um programa que leia vários números inteiros pelo teclado.
          No final da execução, mostre a média entre todos os valores e
          qual foi o maior e menor valor lido. O programa deve perguntar
          ao usuário se ele quer ou não continuar a digitar valores.

Resolução do problema:
"""
op = ''

menor = maior = acumulador = cont = 0

while op != 'N':
    num = int(input('Informe um valor: '))

    op = input('Você deseja informar um novo valor [S/N]: ').strip().upper()

    if cont == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    acumulador += num
    cont += 1

media = acumulador / cont
print('A média dos valores informados é: {:.2f}'.format(media))

print('MENOR VALOR INFORMADO: {}\nMAIOR VALOR INFORMADO: {}'.format(menor, maior))
