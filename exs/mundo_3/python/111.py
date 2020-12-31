"""
Desafio 111

Problema: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados
          moeda e dado.

          Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para
          o primeiro pacote e mantenha tudo funcionando.

Resolução do problema:
"""
from ex111_modulo.utilidadesCeV import moeda

preco = float(input('Informe um preço: R$'))

moeda.resumo(preco, 70, 10)
