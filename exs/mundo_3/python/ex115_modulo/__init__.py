"""
    Arquivo modulazirado do exercício 115.

    Contém todas as funções utilizadas pelo sisteminha,
    desde:
        Impressão do menu inicial;
        Impressão de todos cadastros;
        Realizar novos cadastros e;
        Finalizar o sistema.
"""


def menu():
    from time import sleep
    print('\33[34;1m' + '-' * 40 + f'\n{" MENU ":^40}\n' + '-' * 40 + '\33[m')  # Impressão do cabeçalho do Menu
    print('\33[33;1m1\33[m - \33[30mVer pessoas cadastradas\33[m')
    print('\33[33;1m2\33[m - \33[30mCadastrar nova pessoa\33[m')
    print('\33[33;1m3\33[m - \33[30mSair do sistema\33[m')
    print('\33[34;1m' + '-' * 40 + '\33[m')
    try:
        op = int(input('\33[30mSua Opção:\33[m '))
    except (ValueError, TypeError):
        print('\n\33[31;1mERRO! Opção não existe. Tenta novamente...\33[m')
    else:
        if op == 1:
            sleep(1)
            listar_cadastros()
        elif op == 2:
            sleep(1)
            cadastrar()
        elif op == 3:
            sleep(1)
            finalizar()
        else:
            print('\n\33[31;1mERRO! Opção não existe. Tente novamente...')


def listar_cadastros():
    print('\n\33[36;1m' + '-' * 40 + f'\n{" PESSOAS CADASTRADAS ":^40}\n' + '-' * 40 + '\33[m')  # cabeçalho

    arq_dados = open('ex115_modulo/database.txt', 'r', encoding='utf-8')

    print(f'\33[30;1m{"NOME":<34}{"IDADE":^6}\n\33[m')
    for linha in arq_dados.readlines():
        dados = linha.split()

        nome = ' '.join(dados[:-1])
        idade = dados[-1]

        print(f'\33[30m{nome:<34}{idade:^6}\33[m')
    print('\33[36;1m-' * 40 + '\n')
    arq_dados.close()


def cadastrar():
    import time

    print('\n\33[32;1m' + '-' * 40 + f'\n{" CADASTRAR PESSOA ":^40}\n' + '-' * 40 + '\33[m')  # Impressão do cabeçalho

    arq_dados = open('ex115_modulo/database.txt', 'a', encoding='utf-8')  # Modo de escrita sem excluir conteúdo
    while True:
        try:
            nome = input('\33[30;1mNOME: ').title().strip()
            idade = int(input('IDADE: \33[m'))
        except (ValueError, TypeError):
            print('\n\33[31;1mERRO! Dados inválidos. Tente novamente...\33[m')
            continue

        arq_dados.write(nome + ' ' + str(idade) + '\n')  # Formato padrão: fulano de tal 35\n

        print('\33[30;1m-' * 40)

        novo_cad = input('Novo cadastro ? [S/N]: ').upper().strip()
        while novo_cad not in ('S', 'N'):
            print('\n\33[31mERRO! Opção não existe.\33[m')
            novo_cad = input('Novo cadastro? [S/N]: ').upper().strip()

        print('-' * 40)
        print('\33[32;1mSalvo Com Sucesso!\33[m')
        print('\33[30;1m-' * 40)

        if novo_cad == 'S':
            time.sleep(2)
            continue
        else:
            print('\33[33mEncerrando cadastro(s). . .\33[m\n')
            time.sleep(2)
            break

    arq_dados.close()


def finalizar():
    from time import sleep
    print('\33[34;1m-' * 40)
    print('\33[31;1mFinalizando. . .\33[m\n')
    sleep(3)
    exit(0)
