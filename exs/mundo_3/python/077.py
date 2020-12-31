"""
Desafio 077

Problema: Crie um programa que tenha uma tupla com várias palavras (Não usar acentos).
          Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

Resolução do problema:
"""
# Tupla com todas palavras
palavras = ('carro', 'programar', 'futuro', 'mercado', 'desenvolvimento',
            'ferrari', 'miami', 'brasil', 'python', 'javascript', 'bike',
            'piscina', 'avenida', 'paralelepipedo', 'navio', 'morte')

# Tupla com todas vogais
vogais = ('a', 'e', 'i', 'o', 'u')

# OBS: Sistema de cores ANSI funciona somente no PyCharm que usa
# essa codificação, caso não tenha-o, basta tirar as cores \33[33m excluindo-as
print()

# Descobrindo as vogais de cada palavra
for palavra in palavras:  # Pegando as palavras da tupla uma a uma
    print(f'A palavra \33[33m{palavra.upper()}\33[m tem as vogais: ', end='')
    for letra in palavra:  # Pegando a letra da palavra da tupla
        for vogal in vogais:  # Pegando uma letra da tupla vogais
            if vogal == letra:  # Verificando se a vogal é igual a letra da palavra
                print(f'\33[34m{vogal}\33[m', end=' ')
    print()
