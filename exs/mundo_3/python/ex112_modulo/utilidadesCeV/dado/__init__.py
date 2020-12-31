"""
Desafio 112

Problema: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um
          módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja
          capaz de funcionar como a função input(), mas com uma validação de dados
          para aceitar apenas valores que sejam monetários.

Resolução do problema:
"""


def leiaDinheiro(mensagem):
    """
    -> Verifica se o preço está no formato de dinheiro
    :param mensagem: Mensagem a ser exibida ao usuário
    :return: Retorna o preço convertido para float
    """
    while True:
        preco = input(mensagem).strip()
        analisa_preco = preco

        # Em caso de preco conter vírgula, força substituir por ponto
        if ',' in preco:
            analisa_preco = analisa_preco.replace(',', '.')

        # Dividindo preco onde tem ponto para verificação individual do valor informado
        preco_split = analisa_preco.split('.')

        valido = True

        # Percorrendo a lista gerada ao converter o preco em lista para validação
        for digito in preco_split:
            if not digito.isnumeric():
                valido = False
                break

        # Verificação final
        if not valido or analisa_preco.count('.') > 1:
            print(f'\33[31mERRO: "{preco}" é um preço inválido!\33[m')
            print()
            continue
        else:
            return float(analisa_preco)
