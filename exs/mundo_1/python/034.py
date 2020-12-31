"""
Desafio 034

Problema: Escreva um programa que pergunte o salário de um funcionário
          e calcule o valor do seu aumento. Para salários superiores a
          R$1250,00, calcule um aumento de 10%. Para os inferiores ou
          iguais, o aumento é de 15%.

Resolução do problema:
"""
salario = float(input('Informe seu salário: R$'))

if salario <= 1250.00:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print('O salário com aumento é: R$ {:.2f}'.format(aumento))
