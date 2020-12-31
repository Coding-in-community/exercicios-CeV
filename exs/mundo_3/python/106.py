"""
Desafio 106

Problema: Faça um mini-sistema que utilize o interative Help do Python. O usuário
          vai digitar o comando e o manual vai aparecer. Quando o usuário digitar
          a palavra 'FIM' o programa se encerrará.

          Obs: Use cores.

Resolução do problema:
"""


def header_pyhelp():
    """
    -> Imprime na tela o cabeçalho do PyHelp
    :return: Não possui retorno
    """
    print('\33[30;42m-' * 35 + f'\n{"SISTEMA DE AJUDA PyHelp":^35}\n' + '-' * 35)


def header_search_pyhelp(search):
    """
    -> Imprime na tela o cabeçalho responsivo do manual
    :param search: Parâmetro para receber a palavra pesquisada pelo usuário
    :return: Sem retorno
    """
    header = f'Acessando o manual do comando "{search}"'
    print('\33[30;44m~' * (len(header) + 4))
    print(f'  {header}  ')
    print('~' * (len(header) + 4))


def pyhelp(search):
    """
    -> Realiza uma pesquisa na função/biblioteca escolhida e imprime sua documentação.
    :param search: Parâmetro para receber a palavra pesquisada pelo usuário.
    :return: Retorna a documentação da função/biblioteca pesquisada.
    """
    header_search_pyhelp(search)
    print('\33[37;40m', end='')
    return help(search)


while True:
    header_pyhelp()
    pesquisa = input('\33[mFunção ou Biblioteca >>> ').strip().lower()

    if pesquisa.upper() == 'FIM':
        print('\33[30;41m=' * 20 + f'\n{"FINALIZADO":^20}\n' + '=' * 20)
        break

    pyhelp(pesquisa)
