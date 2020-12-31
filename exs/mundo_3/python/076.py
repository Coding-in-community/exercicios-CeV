"""
Desafio 076

Problema: Crie um programa que tenha uma tupla única com nomes de produtos
          e seus respectivos preços na seguência

          No final, mostre uma listagem de preços, organizando os dados em
          forma tabular.

Resolução do problema:
"""
produtos = ('TV', 1200.00, 'Xbox One', 1450.00, 'Bike', 1000.00,
            'Bolacha', 4.00, 'Leite', 3.99, 'Chocolate', 6.99,
            'PC', 3.480, 'Camiseta', 67.99, 'Notebook', 1699.99,
            'Arroz 5Kg', 8.99, 'Feijão', 5.50, 'Farinha', 4.30)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for idx, prodPreco in enumerate(produtos):
    if idx % 2 == 0:
        # Imprime produto
        print(f'{prodPreco:.<30}', end='')
    else:
        # imprime preço do produto
        print(f'R${prodPreco:>8.2f}')
        
print('-' * 40)