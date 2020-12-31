"""
Desafio 097

Problema: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
          como parâmetro e mostre uma mensagem com o tamanho adaptável.

          Ex: escreva('Olá, Mundo!')

          Saída:
                -------------
                 Olá, Mundo!
                -------------

Resolução do problema:
"""


# Função para imprimir mensagens dentro de cabeçalho com bordas
def escreva(mensagem):
    print('-' * (len(mensagem) + 4))
    print(f'  {mensagem}  ')
    print('-' * (len(mensagem) + 4))


# Cases de chamada da função
escreva('Olá, mundo')
escreva('Python é a melhor linguagem do mundo')
escreva('Python é maior que Java')
