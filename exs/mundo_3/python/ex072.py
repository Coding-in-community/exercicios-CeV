"""
Desafio 072

Problema: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
          por extenso, de zero até vinte.
          Seu programa deverá ler um número pelo teclado (entre 0 e 20)
          e mostrá-los por extenso.

Resolução do problema:
"""
print('-' * 32 + f'\n{" NÚMERO POR EXTENSO ": ^32}\n' + '-' * 32)

numeroPorExtenso = ('zero', 'um', 'dois', 'três', 'quarto', 'cinco',
                    'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
                    'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
                    'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))

    while numero < 0 or numero > 20:
        print('-' * 32 + '\nInforme corretamente o número.')
        numero = int(input('Digite um número entre 0 e 20: '))

    print(f'Você digitou o número {numeroPorExtenso[numero].upper()}')
    print('-' * 32)
    op = input('Outro valor ? [S/N]: ').strip().upper()

    while op != 'N' and op != 'S':
        print('Digite a opção corretamente...')
        op = input('Outro valor ? [S/N]: ').strip().upper()
    print('-' * 32)

    if op == 'N':
        print('Programa finalizado...')
        break
