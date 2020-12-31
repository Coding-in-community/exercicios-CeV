"""
Desafio 111

Problema: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados
          moeda e dado.

          Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para
          o primeiro pacote e mantenha tudo funcionando.

Resolução do problema:
"""


def resumo(valor, bonus, onus):
    """
    -> Print na tela uma tabela formatada com todos os valores e operações realizadas
    :param valor: Valor do dinheiro
    :param bonus: Porcentagem do bônus
    :param onus: Porcentagem do ônus
    :return: Não possui retorno
    """
    print('-' * 35 + f'\n{" RESUMO DO VALOR ":^35}\n' + '-' * 35)

    print(f'Preço analisado:   {moeda(valor)}')
    print(f'Dobro do preço:    {dobro(valor)}')
    print(f'Metade do preço:   {metade(valor)}')
    print(f'{bonus}% de aumento:    {aumentar(valor, bonus)}')
    print(f'{onus}% de redução:    {diminuir(valor, onus)}')

    print('-' * 35)


def moeda(valor):
    """
    -> Realiza formatação do valor passado para dinheiro
    :param valor: Valor do dinheiro
    :return: Retorna o parâmetro passado em formato de reais (R$)
    """
    return f'R${valor:.2f}'.replace('.', ',')


def aumentar(valor, bonus):
    """
    -> Realiza o calculo de aumento sálarial e retorna seu valor
    :param valor: Valor do dinheiro
    :param bonus: Porcentagem do bônus
    :return: Retorna valor com aumento sálarial
    """
    return moeda(valor + (valor * bonus / 100))


def diminuir(valor, onus):
    """
    -> Realiza o calculo de redução salárial e retorna seu valor
    :param valor: Valor do dinheiro
    :param onus: Porcentagem do ônus
    :return: Retorna o valor da redução salárial
    """
    return moeda(valor - (valor * onus / 100))


def dobro(valor):
    """
    -> Realiza o calculo de dobro salárial
    :param valor: Valor do dinheiro
    :return: Retorna o valor dobrado
    """
    return moeda(valor * 2)


def metade(valor):
    """
    -> Realiza o calculo de metade salárial
    :param valor: Valor do dinheiro
    :return: Retorna a metade do valor
    """
    return moeda(valor / 2)
