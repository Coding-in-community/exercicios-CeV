"""
Desafio 112

Problema: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um
          módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja
          capaz de funcionar como a função input(), mas com uma validação de dados
          para aceitar apenas valores que sejam monetários.

Resolução do problema:
"""
from ex112_modulo.utilidadesCeV import moeda
from ex112_modulo.utilidadesCeV import dado

preco = dado.leiaDinheiro('Informe um preço: R$')

moeda.resumo(preco, 65, 25)
