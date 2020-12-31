"""
Desafio 006

Problema: Crie um algoritmo que leia um número e mostre o seu drobro,
          triplo e raiz quadrada.

Resolução do problema:
"""
num = int(input('Informe um valor: '))

dobro = num * 2
triplo = num * 3
raiz = num ** (1 / 2)  # Também pode-se utilizar a função pow(), de sintaxe: pow(num, (1/2))

print('Dobro: {}\nTriplo: {}\nRaiz Quadrada: {:.2f}'.format(dobro, triplo, raiz))
