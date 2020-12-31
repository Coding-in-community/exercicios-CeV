"""
Desafio 113

Problema: Reencreva a função leiaInt() que fizemos no desafio 104, incluindo agora
          a possibilidade da digitação de um número de tipo inválido.
          Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

Resolução do problema:
"""


def leiaInt(msg):
    while True:
        try:
            valor_int = int(input(msg))
            return valor_int
        except (ValueError, TypeError):
            print('\n\33[31mERRO! Informe um valor INTEIRO corretamente...\33[m')
        except KeyboardInterrupt:
            print('\n\33[31mO usuário não informou esse número...\33[m')
            return 0


def leiaFloat(msg):
    while True:
        try:
            valor_float = float(input(msg))
            return valor_float
        except (ValueError, TypeError):
            print('\n\33[31mERRO! Informe um valor FLUTUANTE corretamente...\33[m')
        except KeyboardInterrupt:
            print('\n\33[31mO usuário não informou esse número...\33[m')
            return 0


n_int = leiaInt('Digite um valor inteiro: ')
n_float = leiaFloat('Digite um valor flutuante: ')

print(f'Você digitou como valor inteiro o número: {n_int} e como valor flutuante o número: {n_float}')
