"""
Desafio 107

Problema: Crie um módulo chamado moedas.py que tenha as funções incorporadas
          aumentar(), diminuir(), dobro() e metade().

          Faça também um programa que importe esse módulo e use algumas dessas
          funçóes.

Resolução do problema:
"""


def aumentar(valor, bonus):
    """
    -> Realiza o calculo de aumento sálarial e retorna seu valor
    :param valor: Valor do dinheiro
    :param bonus: Porcentagem do bônus
    :return: Retorna valor com aumento sálarial
    """
    return valor + (valor * bonus / 100)


def diminuir(valor, onus):
    """
    -> Realiza o calculo de redução salárial e retorna seu valor
    :param valor: Valor do dinheiro
    :param onus: Porcentagem do ônus
    :return: Retorna o valor da redução salárial
    """
    return valor - (valor * onus / 100)


def dobro(valor):
    """
    -> Realiza o calculo de dobro salárial
    :param valor: Valor do dinheiro
    :return: Retorna o valor dobrado
    """
    return valor * 2


def metade(valor):
    """
    -> Realiza o calculo de metade salárial
    :param valor: Valor do dinheiro
    :return: Retorna a metade do valor
    """
    return valor / 2
