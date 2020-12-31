"""
Desafio 083

Problema: Crie um programa onde o usuário digite uma expressão qualquer e use
          parênteses. Seu aplicativo deverá analisar se a expressão passada está
          com os parênteses abertos e fechados na ordem correta.

Resolução do problema:
"""
abreParent = []

expressao = input('Digite uma expressão: ').strip().lower()

for caracter in expressao:
    if caracter == '(':
        abreParent.append(caracter)

    if caracter == ')':
        abreParent.pop() if len(abreParent) > 0 else abreParent.append(')')

print('Expressão Correta...' if len(abreParent) == 0 else 'Expressão incorreta...')
