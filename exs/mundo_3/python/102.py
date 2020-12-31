"""
Desafio 102

Problema: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
          o primeiro que indique o número a calcular e o outro chamado show, que será
          um valor lógico(Opcional) indicando se será mostrado ou não na tela o processo
          de cálculo do fatorial.

Resolução do problema:
"""


def header():
    """
    -> Imprime um cabeçalho na tela.
    :return: Sem retorno
    """
    print('-' * 30 + f'\n{"FATORIAL":^30}\n' + '-' * 30)


def fatorial(num, show=False):
    """
    -> Realiza calculo de fatórial de um número inteiro.
    :param num: Parâmetro que recebe o valor a ser calculado o fatórial
    :param show: Parâmetro Opcional, que mostra ou não o calculo do fatórial
    :return: Retorna o valor fatórial de um número inteiro N.
    """
    fato = 1
    for cont in range(num, 0, -1):
        fato *= cont
        if show:
            print(f'{cont}', end=' x ' if cont != 1 else ' = ')
    return fato


print(fatorial(10, True))  # imprimindo calculo e resultado da fatórial do valor informado
print()
print(fatorial(7))  # Imprimindo somente valor retornado pela função fatorial()
print()
help(fatorial)  # Visualizando a docstring da função fatorial()
