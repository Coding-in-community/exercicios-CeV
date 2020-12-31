"""
Desafio 069

Problema: Crie um programa que leia a idade e o sexo de várias
          pessoas. A cada pessoa cadastrada, o programa deverá
          perguntar se o usuário quer ou não continuar.
          No final, mostre:
            A) Quantas pessoas tem mais de 18 anos;
            B) Quantos homens foram cadastrados;
            C) Quantas mulheres tem menos de 20 anos.

Resolução do problema:
"""
contCadastro = qtdPessoa = qtdHomen = qtdMulher = 0

print('-' * 35 + f'\n{" CADASTRO DE PESSOAS ":~^35}\n' + '-' * 35)

while True:
    print(f'\n{contCadastro + 1:2}º CADASTRO ' + '-' * 22)
    idade_usuario = int(input('\nIDADE: '))
    sexo_usuario = input('SEXO [M/F]: ').strip().upper()

    while sexo_usuario != 'M' and sexo_usuario != 'F':
        print('Sexo incorreto, informe novamente...')
        sexo_usuario = input('SEXO [M/F]: ').strip().upper()

    # Pessoas menores de 18 anos
    if idade_usuario > 18:
        qtdPessoa += 1

    # Quantidade de homens
    if sexo_usuario == 'M':
        qtdHomen += 1

    # Quantidade de mulheres menores de 20 anos
    if sexo_usuario == 'F' and idade_usuario < 20:
        qtdMulher += 1

    print('-' * 35)
    novoCadastro = input('Novo cadastro [S/N]: ').strip().upper()

    while novoCadastro != 'S' and novoCadastro != 'N':
        print('-' * 35)
        print('Informa se deseja continuar CORRETAMENTE.')
        novoCadastro = input('Novo cadastro [S/N]: ').strip().upper()

    if novoCadastro == 'N':
        print('\nCADASTROS FINALIZADOS...\n' + '-' * 35)
        break

    print('-' * 35)

    contCadastro += 1

print(f'\n\n{" ESTATÍSTICAS ":-^45}')
print('-' * 45)
print(f'QUANTIDADE DE PESSOAS MAIORES DE 18 ANOS: {qtdPessoa}')
print(f'QUANTIDADE DE HOMENS CADASTRADOS: {qtdHomen}')
print(f'QUANTIDADE DE MULHERES MENORES DE 20 ANOS: {qtdMulher}')
