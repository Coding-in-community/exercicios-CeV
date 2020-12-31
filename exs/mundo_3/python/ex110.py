"""
Desafio 110

Problema: Adicione ao módulo moeda.py criado nos desafios anteriores, uma função
          chamada resumo(). que mostre na tela algumas informações geradas pelas
          funções que já temos no módulo criado até aqui.

Resolução do problema:
"""
from ex110_modulo import moeda

preco = float(input('Informe um preço: R$'))

moeda.resumo(preco, 80, 30)
